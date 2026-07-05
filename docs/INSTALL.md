# CodeX Installation Guide

## Quick Start (3 steps)

### 1. Install the Package
```bash
pip install -e .
```

### 2. Configure API Key
```bash
echo "OPENROUTER_API_KEY=your_actual_key_here" > .env
```

### 3. Run CodeX
```bash
codex "list all files"
```

---

## Detailed Installation

### Prerequisites

- **Python 3.12+** - [Download here](https://www.python.org/downloads/)
- **pip** - Usually comes with Python
- **OpenRouter API Key** - [Get one free](https://openrouter.ai)

### Step 1: Verify Python Installation

```bash
python --version
# Should show: Python 3.12.x or higher
```

If you don't have Python 3.12+, install it or update your current Python.

### Step 2: Clone/Download CodeX

```bash
# If you have git
git clone <repository-url>
cd CodeX

# Or manually download and navigate to the directory
```

### Step 3: Create Virtual Environment (Optional but Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Linux/Mac:
source venv/bin/activate

# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# On Windows (Command Prompt):
venv\Scripts\activate.bat
```

### Step 4: Install CodeX

```bash
# Install in development mode
pip install -e .

# (Optional) Install development tools
pip install -e ".[dev]"

# Verify installation
codex --version
codex --help
```

### Step 5: Set Up API Key

#### Method 1: Using .env file (Recommended)

Create a `.env` file in the CodeX directory:

```bash
echo "OPENROUTER_API_KEY=your_key_here" > .env
```

Or create it manually with these contents:
```
OPENROUTER_API_KEY=your_key_here
```

#### Method 2: Environment Variable

```bash
# Linux/Mac:
export OPENROUTER_API_KEY="your_key_here"

# Windows (PowerShell):
$env:OPENROUTER_API_KEY="your_key_here"

# Windows (Command Prompt):
set OPENROUTER_API_KEY=your_key_here
```

### Step 6: Verify Installation

```bash
# Check CLI is installed
codex --version

# Show help
codex --help

# Test with a simple command
codex "list all files"
```

---

## Troubleshooting

### Command Not Found: `codex`

**Solution:**
```bash
# Make sure you're in the CodeX directory
cd /path/to/CodeX

# Reinstall the package
pip install -e .

# On some systems, you might need to use:
python -m pip install -e .
```

### "OPENROUTER_API_KEY not set"

**Solution:**
1. Verify your .env file exists: `ls -la .env` (Linux/Mac) or `dir .env` (Windows)
2. Check it contains your key: `cat .env` (Linux/Mac) or `type .env` (Windows)
3. Reload your shell or Python environment
4. Test the key is readable:
   ```python
   from dotenv import load_dotenv
   import os
   load_dotenv()
   print(os.environ.get("OPENROUTER_API_KEY"))
   ```

### "ModuleNotFoundError: No module named 'main'"

**Solution:**
```bash
# Make sure you're in the CodeX directory and reinstall:
pwd  # or 'cd' on Windows to verify location
pip install -e .
```

### Virtual Environment Issues

**Solution:**
```bash
# Create a fresh virtual environment
python -m venv venv_new
source venv_new/bin/activate  # Linux/Mac
# OR
.\venv_new\Scripts\Activate.ps1  # Windows PowerShell

# Install again
pip install -e .
```

### API Key Issues

**Solution:**
1. Verify your API key is correct on [OpenRouter](https://openrouter.ai)
2. Check there are no extra spaces or quotes in .env:
   ```
   # WRONG:
   OPENROUTER_API_KEY = "sk-..."
   
   # CORRECT:
   OPENROUTER_API_KEY=sk-...
   ```
3. Try using environment variable instead of .env file

---

## Using the Automated Setup Script

```bash
# Run the setup script
python setup.py

# Follow the interactive prompts
```

This will:
- Verify Python version
- Check for API key configuration
- Install the package
- Optionally install development dependencies
- Provide next steps

---

## Advanced Configuration

### Custom Model

Set a different AI model:
```bash
export CODEX_MODEL="your/model:free"
```

### Custom Working Directory

```bash
export CODEX_WORKING_DIR="/path/to/your/project"
```

### Debug Mode

```bash
export CODEX_DEBUG=true
codex "your command"
```

---

## Uninstall

```bash
# Remove the package
pip uninstall codex-ai

# Remove the directory (optional)
rm -rf CodeX
```

---

## Next Steps

After successful installation, try:

```bash
# See available commands
codex --help

# Try a simple command
codex "list all files in the calculator directory"

# Try reading a file
codex "read main.py"

# For verbose output
codex --verbose "list all files"
```

---

## Getting Help

If you encounter issues:

1. Check the Troubleshooting section above
2. Run with `--verbose` flag for more details
3. Check that your API key is valid
4. Ensure Python 3.12+ is installed
5. Try the setup script: `python setup.py`

---

## Support

For more information:
- See README.md for usage guide
- Check main.py for implementation details
- Review example commands in the README

Happy coding! 🚀
