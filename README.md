# AI Code Doc Generator CLI 🚀

An open-source, automated command-line utility built in Python that leverages lightweight LLM models to analyze local source code files and output structured, standardized Google-style docstrings.

## Features

- **Global CLI Entrypoint:** Execute documentation generation from any directory using the native `ai-doc` shell command.
- **Smart Parsing:** Analyzes Python functions and code structures to determine appropriate documentation layout.
- **Cost-Efficient:** Optimized workflow configured specifically for lightweight, high-performance inference models like `gpt-4o-mini`.

## Installation

Clone the repository and install the utility globally on your system using `pip`:

```bash
git clone https://github.com
cd ai-doc-cli
pip install .
```

*Tip: For development purposes, install using `pip install -e .` so code adjustments refresh automatically.*

## Usage

Set your OpenAI API key and pass your target Python file path straight to the `ai-doc` command:

### macOS / Linux
```bash
export OPENAI_API_KEY="your-api-key-here"
ai-doc path/to/your/script.py
```

### Windows (Command Prompt)
```cmd
set OPENAI_API_KEY="your-api-key-here"
ai-doc path/to/your/script.py
```

### Windows (PowerShell)
```powershell
$env:OPENAI_API_KEY="your-api-key-here"
ai-doc path/to/your/script.py
```

## Contributing

Contributions are welcome! Please open an issue to discuss proposed features or structural changes before submitting a pull request. 

## License

This utility is maintained under the **Apache License 2.0**. See the `LICENSE` file for more details.
