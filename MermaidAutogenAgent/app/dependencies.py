# This file can be used for dependency injection and utility functions.
from .config_manager import ConfigManager

def get_config():
    return ConfigManager.get_config()
