"""
Penguin Data Analyzer - Main Entry Point
A command-line application to manage and analyze penguin datasets.

Lab 11-12: Algorithms Fundamentals
"""
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from repository.penguin_repo import PenguinRepo
from repository.penguin_repo_file import PenguinRepoFile
from service.penguin_service import PenguinService
from service.stats_service import StatsService
from service.classifier_service import ClassifierService
from ui.console import Console


def preprocess_data():
    """
    Preprocess raw penguins.csv to create penguins_data.csv
    This should be run before the main application if working with raw data.
    """
    file_repo = PenguinRepoFile("data")
    repo = PenguinRepo()
    service = PenguinService(repo, file_repo)
    
    try:
        count = service.preprocess_data("penguins.csv", "penguins_data.csv")
        print(f"Preprocessing complete: {count} valid rows saved to penguins_data.csv")
    except Exception as e:
        print(f"Preprocessing failed: {e}")
        print("Make sure 'penguins.csv' exists in the 'data' directory.")


def run_tests():
    """Run all unit tests"""
    from all_tests.run_all_tests import run_all_tests
    result = run_all_tests()
    return result.wasSuccessful()


def main():
    """Main application entry point"""
    # Check command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == '--preprocess':
            preprocess_data()
            return
        elif sys.argv[1] == '--test':
            success = run_tests()
            sys.exit(0 if success else 1)
        elif sys.argv[1] == '--help':
            print("Penguin Data Analyzer")
            print("=" * 40)
            print("Usage:")
            print("  python main.py           - Run the application")
            print("  python main.py --preprocess - Preprocess raw data")
            print("  python main.py --test    - Run unit tests")
            print("  python main.py --help    - Show this help")
            return

    # Initialize components
    penguin_repo = PenguinRepo()
    penguin_repo_file = PenguinRepoFile("data")
    
    penguin_service = PenguinService(penguin_repo, penguin_repo_file)
    stats_service = StatsService(penguin_repo)
    classifier_service = ClassifierService(penguin_repo)
    
    # Create and run console
    console = Console(penguin_service, stats_service, classifier_service)
    console.run()


if __name__ == '__main__':
    main()
