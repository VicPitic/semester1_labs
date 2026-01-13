from manager.manager import MyStringManager
from ui.Console import Console


def main():
    """Run the MyString Manager application."""
    # Create a manager
    manager = MyStringManager()
    
    # Create and run the console UI
    console = Console(manager)
    console.run()


if __name__ == '__main__':
    main()
