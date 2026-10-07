"""Command-line decoder for Unicode coordinate grids in published Google Docs."""

from __future__ import annotations

import argparse
import html
import sys
from html.parser import HTMLParser
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class _TableParser(HTMLParser):
    """Collect text cells from every HTML table row."""

    def __init__(self) -> None:
        super().__init__()
        self.rows: list[list[str]] = []
        self._row: list[str] | None = None
        self._cell: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "tr":
            self._row = []
        elif tag in {"td", "th"} and self._row is not None:
            self._cell = []

    def handle_data(self, data: str) -> None:
        if self._cell is not None:
            self._cell.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag in {"td", "th"} and self._cell is not None and self._row is not None:
            self._row.append(html.unescape("".join(self._cell)).strip())
            self._cell = None
        elif tag == "tr" and self._row is not None:
            if self._row:
                self.rows.append(self._row)
            self._row = None


def fetch_document(url: str, timeout: float = 15.0) -> str:
    """Download a published Google Doc and return its HTML."""
    request = Request(url, headers={"User-Agent": "ai-doc-cli/1.0"})
    with urlopen(request, timeout=timeout) as response:
        return response.read().decode(response.headers.get_content_charset() or "utf-8")


def parse_points(document_html: str) -> dict[tuple[int, int], str]:
    """Parse x-coordinate, character, y-coordinate rows from document HTML."""
    parser = _TableParser()
    parser.feed(document_html)
    points: dict[tuple[int, int], str] = {}

    for row in parser.rows:
        if len(row) < 3:
            continue
        try:
            x, y = int(row[0]), int(row[2])
        except ValueError:  # Header row or unrelated table content.
            continue
        if x < 0 or y < 0:
            raise ValueError("Coordinates must be non-negative")
        points[(x, y)] = row[1]

    if not points:
        raise ValueError("No coordinate rows were found in the document")
    return points


def render_grid(points: dict[tuple[int, int], str]) -> str:
    """Render points with the highest y-coordinate on the first printed row."""
    max_x = max(x for x, _ in points)
    max_y = max(y for _, y in points)
    lines = []
    for y in range(max_y, -1, -1):
        lines.append("".join(points.get((x, y), " ") for x in range(max_x + 1)).rstrip())
    return "\n".join(lines)


def decode_document(url: str) -> str:
    """Fetch, parse, and render a published Google Doc grid."""
    return render_grid(parse_points(fetch_document(url)))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ai-doc-cli",
        description="Print the Unicode grid stored in a published Google Doc.",
    )
    parser.add_argument("url", help="Published Google Doc URL ending in /pub")
    parser.add_argument("--timeout", type=float, default=15.0, help="Request timeout in seconds")
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        print(render_grid(parse_points(fetch_document(args.url, args.timeout))))
    except (HTTPError, URLError, TimeoutError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
