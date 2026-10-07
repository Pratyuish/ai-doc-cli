# AI Code Doc Generator CLI 🚀

An open-source, automated command-line utility built in Python that leverages lightweight LLM models to analyze local source code files and output structured, standardized Google-style docstrings.

## Features

- **Global CLI Entrypoint:** Execute documentation generation from any directory using the native `ai-doc` shell command.
- **Smart Parsing:** Analyzes Python functions and code structures to determine appropriate documentation layout.
- **Cost-Efficient:** Optimized workflow configured specifically for lightweight, high-performance inference models like `gpt-4o-mini`.

## Installation

To comply with modern Python packaging guidelines (PEP 668) and avoid environment conflicts, it is highly recommended to install this utility within an isolated virtual environment.

### 1. Clone and Set Up Environment
```bash
# Clone the repository
git clone https://github.com
cd ai-doc-cli

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 2. Install the Package
```bash
# Install universally inside your active environment
pip install .
```

*Tip: For development and testing purposes, install using `pip install -e .` so code adjustments refresh instantly without a reinstall.*

## Usage

Ensure your virtual environment is active, set your OpenAI API key, and pass your target Python file path straight to the `ai-doc` command:

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
