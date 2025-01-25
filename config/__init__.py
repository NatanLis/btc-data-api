import configparser
import os

def load_config(filename):
    """
    Load a .cfg configuration file from the config directory.

    Args:
        filename (str): Name of the .cfg file (e.g., 'database.cfg').

    Returns:
        configparser.ConfigParser: Loaded configuration object.
    """
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), filename)
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file {filename} not found in the config directory.")
    config.read(config_path)
    return config
