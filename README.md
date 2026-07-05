# CodeX - AI Coding Assistant CLI

A powerful command-line tool powered by AI that helps you manage, read, write, and execute code files intelligently. CodeX acts as your pair programmer right in the terminal, capable of interacting directly with your local file system.

## ✨ Quick Start

```bash
# 1. Install via pip (editable mode recommended)
pip install -e .

# 2. Configure your API Key
echo "OPENROUTER_API_KEY=your_key" > .env

# 3. Use the CLI
codex "list all files in the calculator directory"
codex "read main.py and explain it"
codex --help
```

## 🧠 How CodeX Works: In-Depth Agent Flow

CodeX utilizes an autonomous agent loop powered by an LLM (Large Language Model) to iteratively solve your coding tasks. Here is the step-by-step flow of how the agent operates:

1. **Initialization & Context**: When you run `codex "your task"`, the CLI initializes the environment, loads your `.env` variables (like `OPENROUTER_API_KEY`), and constructs the initial message context. This context includes a robust system prompt defining the agent's persona and constraints, your specific task, and a list of available tool schemas.
2. **LLM Inference**: The agent queries the LLM (default: `nvidia/nemotron-3-nano-30b-a3b:free` via OpenRouter) with the current conversation history.
3. **Tool Evaluation**: The LLM analyzes the task and decides whether it needs to interact with your local environment to proceed. If it does, it outputs a structured `tool_call` requesting to execute a specific function.
4. **Local Execution**: CodeX intercepts this `tool_call`, extracts the function name and arguments, and safely executes the corresponding local Python function (e.g., `write_file`, `run_python_file`).
5. **Feedback Loop**: The stdout/stderr or return value of the local function is captured and appended to the conversation history as a `tool` response.
6. **Iterative Problem Solving**: The agent loops back to Step 2, passing the new context (including the tool's result) to the LLM. This iterative loop (up to 20 iterations) continues until the LLM gathers all necessary information and successfully completes the task.
7. **Final Response**: Once the task is completed and no more tools are required, the LLM generates a final natural language response, which is presented to you in the terminal.

### 🛠️ Available Tools (Capabilities)
- **`get_files_info`**: Explores directories and retrieves file metadata (size, type).
- **`get_file_content`**: Safely reads the contents of local files up to a specified character limit to prevent context overflow.
- **`write_file`**: Creates or overwrites files with new code or text.
- **`run_python_file`**: Executes Python scripts locally, capturing stdout and stderr to verify code correctness.

## 📁 Project Structure

```text
CodeX/
├── src/codex/                    # Main CLI package and agent loop logic
│   ├── cli.py                    # Entry point for the `codex` command
│   ├── main.py                   # Agent loop, LLM integration, and tool dispatcher
│   ├── config.py                 # Constants and configuration
│   ├── call_function.py          # Secure local function router
│   └── prompts.py                # System prompts for the LLM
│
├── functions/                    # Local tool implementations and schemas
│   ├── get_files_info.py
│   ├── get_file_content.py
│   ├── write_file.py
│   └── run_python_file.py
│
├── calculator/                   # Sandbox/example project
├── tests/                        # Test suite for local functions
└── pyproject.toml                # Project packaging and dependencies
```

## 🚀 Features

- 🤖 **Autonomous Agent Loop**: Solves complex tasks iteratively by planning and executing multiple steps.
- 📁 **File Management**: Navigates your workspace to find relevant context.
- 💻 **Code Analysis**: Reads and explains existing codebases.
- ✍️ **Code Generation**: Writes and modifies files directly.
- ▶️ **Code Execution**: Runs Python files and uses the output to debug errors autonomously.
- 🛡️ **Safe Execution**: All tools are scoped to the current working directory to prevent path traversal outside your workspace.

## 🔧 Installation

### Recommended: Editable Install
```bash
# Navigate to the CodeX repository and run:
pip install -e .
```

### With Development Tools (for contributing)
```bash
pip install -e ".[dev]"
```

## 💻 Usage

```bash
# Basic usage
codex "Refactor the get_file_content function to handle binary files"

# Verbose mode (see every tool call and iteration)
codex --verbose "run tests.py and fix any failing tests"

# Show version
codex --version
```

## ⚙️ Configuration

CodeX uses environment variables for configuration. Create a `.env` file in your working directory:
```env
OPENROUTER_API_KEY=your_openrouter_api_key
```
*Note: You can modify `src/codex/main.py` to change the default LLM model or use a different OpenAI-compatible provider.*

## 🧪 Testing

Run the local test suite using `pytest`:
```bash
pytest tests/
```

## 📄 License

MIT License - See docs for details.

## 🤝 Contributing

Contributions are welcome! If you'd like to add new tools or support other languages (e.g., `run_node_file`), please open an issue or pull request.
