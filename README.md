# AI Doc CLI

[![Tests](https://github.com/Pratyuish/ai-doc-cli/actions/workflows/test.yml/badge.svg)](https://github.com/Pratyuish/ai-doc-cli/actions/workflows/test.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

A small, dependency-free Python CLI that decodes a Unicode character grid from
a published Google Doc. Each document row supplies an `x` coordinate, a
Unicode character, and a `y` coordinate; unspecified positions are rendered as
spaces.

## Project structure

```text
ai-doc-cli/
├── .github/workflows/test.yml
├── doc_generator/
│   ├── __init__.py
│   └── cli.py
├── LICENSE
├── README.md
└── requirements.txt
```

## Requirements

- Python 3.10 or newer
- A published Google Doc containing the coordinate table

## Usage

```bash
git clone https://github.com/Pratyuish/ai-doc-cli.git
cd ai-doc-cli
python -m doc_generator.cli "https://docs.google.com/document/d/e/.../pub"
```

Set a custom request timeout when needed:

```bash
python -m doc_generator.cli "YOUR_PUBLISHED_DOC_URL" --timeout 30
```

## Python API

```python
from doc_generator.cli import decode_document

message = decode_document("YOUR_PUBLISHED_DOC_URL")
print(message)
```

## How it works

1. Downloads the published document HTML.
2. Reads table rows in `x-coordinate`, `character`, `y-coordinate` order.
3. Builds a grid from `(0, 0)` to the largest supplied coordinates.
4. Fills missing positions with spaces and prints rows from top to bottom.

## Continuous integration

GitHub Actions checks Python 3.10 through 3.13, compiles the package, and runs
a CLI smoke test on every push and pull request.

## License

Released under the [Apache License 2.0](LICENSE).
