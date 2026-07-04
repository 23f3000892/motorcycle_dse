"""
Main entry point for the Motorcycle Design Space Exploration platform.

Current Version:
- Loads project configuration
- Displays startup information

Author: Devadarshan & ChatGPT
"""

from config.config_loader import ConfigLoader


def main():
    """Main program entry."""

    print("=" * 50)
    print(" Motorcycle Design Space Exploration")
    print("=" * 50)

    loader = ConfigLoader("config/config.yaml")
    config = loader.load()

    print("\nConfiguration loaded successfully!\n")

    print(f"Project : {config['project']['name']}")
    print(f"Version : {config['project']['version']}")

    print("\nLoaded Sections:")

    for section in config:
        print(f"  - {section}")

    print("\nReady for Design Space Generation.")


if __name__ == "__main__":
    main()