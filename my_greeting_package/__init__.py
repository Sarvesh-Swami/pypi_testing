"""
A simple package that prints a greeting message.
"""

__version__ = "0.1.0"

def greet():
    """Print a greeting message to the terminal."""
    print("=" * 50)
    print("🎉 Hello from My Greeting Package! 🎉")
    print("=" * 50)
    print("Thank you for installing my package!")
    print("This is a simple demo package published on PyPI.")
    print("=" * 50)

def main():
    """Entry point for the command-line interface."""
    greet()

if __name__ == "__main__":
    main()
