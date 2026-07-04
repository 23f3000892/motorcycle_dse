"""
Configuration Loader Module

This module is responsible for loading the project's YAML configuration
file and returning it as a Python dictionary.

Responsibilities:
- Verify configuration file exists
- Load YAML safely
- Validate that it is not empty

Author: Devadarshan & ChatGPT
Project: Motorcycle Design Space Exploration
"""

from pathlib import Path
import yaml


class ConfigLoader:
    """Loads the project configuration from a YAML file."""

    def __init__(self, config_path: str):
        self.config_path = Path(config_path)

    def load(self) -> dict:
        """
        Load the YAML configuration file.

        Returns
        -------
        dict
            Parsed configuration data.

        Raises
        ------
        FileNotFoundError
            If the configuration file does not exist.

        ValueError
            If the configuration file is empty.
        """

        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found:\n{self.config_path}"
            )

        with self.config_path.open("r", encoding="utf-8") as file:
            config = yaml.safe_load(file)

        if config is None:
            raise ValueError("Configuration file is empty.")

        return config