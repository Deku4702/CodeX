# CodeX CLI - Usage Examples

This document provides practical examples of using the CodeX CLI for various tasks.

## Table of Contents
1. [File Exploration](#file-exploration)
2. [Code Reading](#code-reading)
3. [File Creation](#file-creation)
4. [Code Execution](#code-execution)
5. [Analysis & Debugging](#analysis--debugging)
6. [Advanced Usage](#advanced-usage)

---

## File Exploration

### List directory contents
```bash
codex "list all files in the calculator directory"
codex "show me what files are in the project"
codex "what's in the functions folder?"
```

### Explore project structure
```bash
codex "show the overall structure of this project"
codex "list all Python files in the project"
codex "find all text files"
```

### Get file information
```bash
codex "how many files are in the calculator directory?"
codex "what files contain tests?"
codex "show me the directory structure"
```

---

## Code Reading

### Read entire files
```bash
codex "read main.py"
codex "show me the content of hello.py"
codex "display the calculator.py file"
```

### Understand code
```bash
codex "read main.py and explain what it does"
codex "what does the hello.py file do?"
codex "explain the code in tests.py"
```

### Find specific functions
```bash
codex "read calculator.py and show me the main function"
codex "what functions are available in render.py?"
codex "find the test functions in tests.py"
```

### Compare files
```bash
codex "read main.py and compare it to hello.py"
codex "what are the differences between calculator.py and render.py?"
```

---

## File Creation

### Create simple files
```bash
codex "create a file called test.py with a simple hello world function"
codex "write a new file called utils.py with some utility functions"
```

### Create with specific content
```bash
codex "create a file called config.py that contains configuration variables for the app"
codex "write a file called constants.py with common constants used in the project"
```

### Create documentation
```bash
codex "create a README.md file explaining this project"
codex "write CONTRIBUTING.md with guidelines for contributing"
```

### Create code structures
```bash
codex "create a new class called DataProcessor in a file called processor.py"
codex "write a Python module with functions for file handling"
```

---

## Code Execution

### Run tests
```bash
codex "run tests.py"
codex "execute the test suite and show me the results"
codex "run tests.py and tell me if they pass"
```

### Run scripts
```bash
codex "run main.py"
codex "execute hello.py"
codex "run the python script in the calculator directory"
```

### Run with output
```bash
codex "execute primeChecker.ts... wait, run the Python equivalent and show results"
codex "run main.py and capture all output"
```

### Debug execution
```bash
codex --verbose "run tests.py and show detailed execution logs"
codex --verbose "execute main.py with all intermediate steps shown"
```

---

## Analysis & Debugging

### Bug identification
```bash
codex "read tests.py and identify any bugs"
codex "analyze calculator.py for potential issues"
codex "check main.py for errors"
```

### Code quality
```bash
codex "review the code in hello.py for improvements"
codex "what best practices could improve this code in render.py?"
codex "suggest optimizations for the calculator.py"
```

### Error resolution
```bash
codex "read the error output and help me fix it"
codex "run tests.py and fix any failing tests"
codex "execute main.py, identify errors, and provide fixes"
```

### Verify functionality
```bash
codex "run tests.py to verify everything works"
codex "execute hello.py and verify it produces the expected output"
```

---

## Advanced Usage

### Multi-step tasks
```bash
codex "read main.py, understand it, then create a test file that tests its functions"
codex "list the files, read each one, then create comprehensive documentation"
```

### Create and test
```bash
codex "create a new function in calculator.py that checks prime numbers, then test it"
codex "write new code in utils.py, then run tests.py to verify it works"
```

### Refactoring
```bash
codex "read main.py, identify issues, refactor it, and create tests"
codex "clean up and optimize the calculator.py file"
```

### Documentation generation
```bash
codex "read all Python files and create comprehensive documentation"
codex "generate a usage guide based on the current code"
```

### Project setup
```bash
codex "read the current project structure and create necessary config files"
codex "set up a proper project structure with necessary utility files"
```

---

## Verbose Mode Examples

Use `--verbose` or `-v` to see detailed execution steps:

```bash
# See each iteration of the AI thinking
codex --verbose "read main.py and explain it"

# Track function calls being made
codex -v "list files and read main.py"

# Debug complex operations
codex --verbose "analyze the code and create tests"
```

---

## Tips & Tricks

### Combine operations
```bash
# Read multiple files then create a summary
codex "read main.py and hello.py, then create a summary"

# Explore, analyze, and suggest fixes
codex "list files, find issues, and propose solutions"
```

### Use specific paths
```bash
codex "read calculator/main.py"
codex "list files in calculator/pkg"
codex "run calculator/tests.py"
```

### Ask for help
```bash
codex "what should I do with this project?"
codex "how can I improve calculator.py?"
codex "what functions should I add?"
```

### Check results
```bash
# After any operation, ask for verification
codex "did that work correctly?"
codex "verify the changes were applied"
codex "run tests to confirm it works"
```

---

## Common Workflows

### Setup workflow
```bash
codex "explore the project structure"
codex "read the main files to understand what it does"
codex "identify any issues or improvements needed"
```

### Testing workflow
```bash
codex "run tests.py"
codex "identify any failing tests"
codex "fix the failing tests"
codex "run tests.py again to confirm"
```

### Development workflow
```bash
codex "create a new feature in [filename]"
codex "run tests.py to verify it works"
codex "create documentation for the new feature"
```

### Debugging workflow
```bash
codex "run [script].py and capture any errors"
codex "analyze the error and identify the cause"
codex "suggest and implement a fix"
codex "run again to confirm the fix works"
```

---

## Troubleshooting

### Long responses
- Use `--verbose` to see what's happening
- Break complex tasks into smaller ones

### Unexpected results
- Rephrase your request more specifically
- Provide more context about what you want
- Use simpler, clearer language

### Timeouts
- Try a simpler task first
- Check your internet connection
- Verify your API key is valid

---

## More Help

- See README.md for feature overview
- See INSTALL.md for installation help
- Run `codex --help` for command-line options
- Run `codex --version` to check your version

Happy coding with CodeX! 🚀
