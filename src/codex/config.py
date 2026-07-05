"""
Configuration module for CodeX CLI.
Handles environment and application settings.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Application configuration."""
    
    # API Configuration
    OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
    OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
    
    # Model Configuration
    MODEL = os.environ.get("CODEX_MODEL", "nvidia/nemotron-3-nano-30b-a3b:free")
    TEMPERATURE = float(os.environ.get("CODEX_TEMPERATURE", "0"))
    MAX_ITERATIONS = int(os.environ.get("CODEX_MAX_ITERATIONS", "20"))
    
    # Working Directory
    WORKING_DIR = os.environ.get("CODEX_WORKING_DIR", "./calculator")
    
    # Debug/Logging
    DEBUG = os.environ.get("CODEX_DEBUG", "false").lower() == "true"
    VERBOSE = False  # Set by CLI arguments
    
    @classmethod
    def validate(cls):
        """Validate that required configuration is set."""
        if not cls.OPENROUTER_API_KEY:
            raise RuntimeError(
                "OPENROUTER_API_KEY environment variable is not set. "
                "Please set it in .env or export it in your shell."
            )
        return True
    
    @classmethod
    def to_dict(cls):
        """Return configuration as a dictionary."""
        return {
            "api_key_set": bool(cls.OPENROUTER_API_KEY),
            "model": cls.MODEL,
            "temperature": cls.TEMPERATURE,
            "max_iterations": cls.MAX_ITERATIONS,
            "working_dir": cls.WORKING_DIR,
            "debug": cls.DEBUG,
        }


# Export configuration instance
config = Config()
