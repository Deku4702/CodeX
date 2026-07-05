#!/usr/bin/env python3
"""
Quick start script for CodeX CLI.
Runs a simple setup and provides usage instructions.
"""

import sys
import subprocess
from pathlib import Path


def main():
    print("""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║                    CodeX CLI Quick Start                      ║
║                                                               ║
║          An intelligent coding assistant powered by AI        ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    """)

    # Check if package is installed
    try:
        subprocess.run([sys.executable, "-m", "pip", "show", "codex-ai"], 
                      capture_output=True, check=True)
        print("✓ CodeX is installed\n")
    except subprocess.CalledProcessError:
        print("⚠ CodeX not installed yet. Installing...\n")
        subprocess.run([sys.executable, "-m", "pip", "install", "-e", "."])
        print()

    # Check for API key
    env_file = Path(".env")
    if env_file.exists():
        print("✓ .env file found")
    else:
        print("⚠ .env file not found. Creating template...\n")
        env_file.write_text("OPENROUTER_API_KEY=your_key_here\n")
        print("  Please edit .env and add your OpenRouter API key\n")

    print("=" * 63)
    print("Ready to use CodeX! Try these commands:\n")
    print("Get help:")
    print("  $ codex --help\n")
    print("List files:")
    print("  $ codex \"list all files in the calculator directory\"\n")
    print("Read a file:")
    print("  $ codex \"read main.py and explain it\"\n")
    print("Create a file:")
    print("  $ codex \"create a new file called test.py\"\n")
    print("Run tests:")
    print("  $ codex \"run tests.py\"\n")
    print("Use verbose mode:")
    print("  $ codex --verbose \"list all files\"\n")
    print("=" * 63)
    print("\nFor more examples, see EXAMPLES.md")
    print("For installation help, see INSTALL.md")
    print("For full documentation, see README.md\n")


if __name__ == "__main__":
    main()
