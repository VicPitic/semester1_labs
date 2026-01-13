"""
Run all tests for the Penguin Data Application
"""
import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from all_tests.test_domain import TestPenguin, TestPenguinValidator
from all_tests.test_repo import TestPenguinRepo
from all_tests.test_service import (
    TestPenguinServiceFilter,
    TestPenguinServiceDescribe,
    TestPenguinServiceUnique,
    TestPenguinServiceSort
)


def run_all_tests():
    """Run all unit tests and return results"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add domain tests
    suite.addTests(loader.loadTestsFromTestCase(TestPenguin))
    suite.addTests(loader.loadTestsFromTestCase(TestPenguinValidator))

    # Add repository tests
    suite.addTests(loader.loadTestsFromTestCase(TestPenguinRepo))

    # Add service tests
    suite.addTests(loader.loadTestsFromTestCase(TestPenguinServiceFilter))
    suite.addTests(loader.loadTestsFromTestCase(TestPenguinServiceDescribe))
    suite.addTests(loader.loadTestsFromTestCase(TestPenguinServiceUnique))
    suite.addTests(loader.loadTestsFromTestCase(TestPenguinServiceSort))

    # Run tests with verbosity
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return result


def run_quick_tests():
    """Run quick functional tests without unittest framework"""
    print("=" * 60)
    print("Running Quick Functional Tests")
    print("=" * 60)

    from domain.penguin import Penguin
    from repository.penguin_repo import PenguinRepo

    # Test Penguin creation
    penguin = Penguin("Adelie", 181.0, 39.1, 18.7, 3750.0, "Torgersen", "MALE")
    assert penguin.get_species() == "Adelie"
    assert penguin.get_flipper_length_mm() == 181.0
    print("✓ Penguin creation test passed")

    # Test Penguin getters/setters
    penguin.set_species("Gentoo")
    assert penguin.get_species() == "Gentoo"
    print("✓ Penguin setters test passed")

    # Test Repository
    repo = PenguinRepo()
    repo.add_penguin(penguin)
    assert repo.get_penguin_count() == 1
    print("✓ Repository add test passed")

    # Test filter
    p2 = Penguin("Chinstrap", 200.0, 45.0, 17.0, 4500.0, "Dream", "FEMALE")
    repo.add_penguin(p2)
    filtered = repo.get_penguins_by_filter('body_mass_g', 4000.0, True)
    assert len(filtered) == 1
    assert filtered[0].get_species() == "Chinstrap"
    print("✓ Filter test passed")

    print("=" * 60)
    print("All quick tests passed!")
    print("=" * 60)


if __name__ == '__main__':
    # Run quick tests first
    run_quick_tests()
    print()

    # Run full unittest suite
    result = run_all_tests()

    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)
