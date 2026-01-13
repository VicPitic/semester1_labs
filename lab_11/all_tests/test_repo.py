"""
Tests for Repository layer - PenguinRepo
"""
import unittest
from domain.penguin import Penguin
from repository.penguin_repo import PenguinRepo


class TestPenguinRepo(unittest.TestCase):
    """Test cases for PenguinRepo"""

    def setUp(self):
        """Set up test fixtures"""
        self.repo = PenguinRepo()
        
        # Create sample penguins
        self.penguin1 = Penguin("Adelie", 181.0, 39.1, 18.7, 3750.0, "Torgersen", "MALE")
        self.penguin2 = Penguin("Gentoo", 217.0, 46.1, 13.2, 4950.0, "Biscoe", "FEMALE")
        self.penguin3 = Penguin("Chinstrap", 195.0, 49.0, 19.5, 3950.0, "Dream", "MALE")

    def test_add_penguin(self):
        """Test adding a penguin"""
        self.repo.add_penguin(self.penguin1)
        
        self.assertEqual(self.repo.get_penguin_count(), 1)
        self.assertIn(self.penguin1, self.repo.get_all_penguins())

    def test_add_all(self):
        """Test adding multiple penguins"""
        penguins = [self.penguin1, self.penguin2, self.penguin3]
        self.repo.add_all(penguins)
        
        self.assertEqual(self.repo.get_penguin_count(), 3)

    def test_clear(self):
        """Test clearing the repository"""
        self.repo.add_all([self.penguin1, self.penguin2])
        self.repo.clear()
        
        self.assertEqual(self.repo.get_penguin_count(), 0)

    def test_set_penguins(self):
        """Test replacing all penguins"""
        self.repo.add_penguin(self.penguin1)
        self.repo.set_penguins([self.penguin2, self.penguin3])
        
        self.assertEqual(self.repo.get_penguin_count(), 2)
        self.assertNotIn(self.penguin1, self.repo.get_all_penguins())

    def test_filter_numeric_greater(self):
        """Test numeric filter (greater than)"""
        self.repo.add_all([self.penguin1, self.penguin2, self.penguin3])
        
        # Filter penguins with body_mass > 4000
        result = self.repo.get_penguins_by_filter('body_mass_g', 4000.0, True)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_species(), "Gentoo")

    def test_filter_string_equal(self):
        """Test string filter (equal)"""
        self.repo.add_all([self.penguin1, self.penguin2, self.penguin3])
        
        # Filter penguins on Torgersen island
        result = self.repo.get_penguins_by_filter('island', 'Torgersen', False)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_species(), "Adelie")

    def test_get_attribute_values(self):
        """Test getting all values for an attribute"""
        self.repo.add_all([self.penguin1, self.penguin2, self.penguin3])
        
        species_values = self.repo.get_attribute_values('species')
        
        self.assertEqual(len(species_values), 3)
        self.assertIn("Adelie", species_values)
        self.assertIn("Gentoo", species_values)


if __name__ == '__main__':
    unittest.main()
