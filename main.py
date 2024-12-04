"""main.py
The entry point for the application.

This module handles the initialization and execution of the project.
Make sure to organize imports and configurations correctly."""

from config import PAUSE
from dna import animate_dna


def main():
    """The main function that initiates the DNA animation."""
    try:
        animate_dna(PAUSE)
    except KeyboardInterrupt:
        print("\nAnimation stopped.")


if __name__ == '__main__':
    main()
