# CodeX - AI Coding Assistant CLI

A powerful command-line tool powered by AI that helps you manage, read, write, and execute code files intelligently.

## Features

- 🤖 **AI-Powered Assistance** - Leverages advanced AI models to understand and execute your requests
- 📁 **File Management** - Explore, read, and write files with natural language commands
- 🔍 **Code Analysis** - Understand and analyze your codebase
- ▶️ **Code Execution** - Run Python files and scripts safely
- 💬 **Natural Language Interface** - Communicate with your code naturally

## Installation

### Prerequisites
- Python 3.12 or higher
- OpenRouter API key

### Setup

1. Clone or download the repository:
```bash
cd CodeX
```

2. Install the package in development mode:
```bash
pip install -e .
```

3. Set up your API key:
```bash
# Create a .env file in the project root
echo "OPENROUTER_API_KEY=your_key_here" > .env
```

Or export it directly:
```bash
export OPENROUTER_API_KEY=your_key_here
```

## Usage

### Basic Command Structure

```bash
codex "your command here"
```

### Examples

#### List files and explore your project
```bash
codex "list all files in the calculator directory"
codex "show me the structure of the project"
```

#### Read and understand code
```bash
codex "read main.py and explain what it does"
codex "what's in the hello.py file?"
```

#### Create and write files
```bash
codex "create a new file called test.py with a hello world function"
codex "write a function that checks if a number is prime"
```

#### Run and test code
```bash
codex "run tests.py and show me the results"
codex "execute the calculator main.py with arguments"
```

### Command-Line Options

```bash
codex --help                    # Show help message
codex --version                 # Show version
codex --verbose "your command"  # Enable verbose output
codex -v "your command"         # Short form of --verbose
```

## Available Tools

The AI agent has access to the following tools:

### `get_files_info`
- **Purpose**: List files and directories
- **Example**: "What files are in the calculator folder?"

### `get_file_content`
- **Purpose**: Read file contents
- **Example**: "Show me the content of main.py"

### `write_file`
- **Purpose**: Create or modify files
- **Example**: "Create a new file called utils.py with..."

### `run_python_file`
- **Purpose**: Execute Python files
- **Example**: "Run the tests.py file"

## Project Structure

```
CodeX/
├── main.py              # CLI entry point
├── prompts.py           # System prompts for the AI
├── call_function.py     # Function calling logic
├── pyproject.toml       # Project configuration
├── functions/           # Tool implementations
│   ├── get_files_info.py
│   ├── get_file_content.py
│   ├── write_file.py
│   └── run_python_file.py
└── calculator/          # Example project
    ├── main.py
    ├── tests.py
    └── pkg/
```

## Environment Variables

- `OPENROUTER_API_KEY` (Required) - Your OpenRouter API key for AI model access

## Configuration

Edit `main.py` to change:
- **Model**: `nvidia/nemotron-3-nano-30b-a3b:free` (line ~95)
- **Max Iterations**: `20` (line ~97)
- **Temperature**: `0` (line ~108) - Controls randomness of responses

## Development

### Install Development Dependencies

```bash
pip install -e ".[dev]"
```

### Run Tests

```bash
pytest
```

### Code Quality

```bash
black .           # Format code
ruff check .      # Lint code
```

## Troubleshooting

### "OPENROUTER_API_KEY not set"
- Make sure your `.env` file exists in the project root
- Check that `OPENROUTER_API_KEY` is set correctly
- Use `echo $OPENROUTER_API_KEY` to verify it's accessible

### Command not recognized
- Ensure the package is installed: `pip install -e .`
- Try using full paths: `python main.py "your command"`

### AI takes too long to respond
- Use `--verbose` to see iteration progress
- Check your internet connection
- Verify your API key is valid

## Contributing

Contributions are welcome! Please ensure:
- Code follows PEP 8 standards
- Tests are included for new features
- Documentation is updated

## License

MIT License - See LICENSE file for details

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the examples above
3. Run with `--verbose` for detailed output

## Version

Current Version: 0.1.0 (Alpha)

---

**Built with ❤️ by the CodeX team**
