"""
Tests for Service layer - PenguinService
Specifically tests filter, describe, and unique functionalities
"""
import unittest
from domain.penguin import Penguin
from domain.exceptions import (
    NoDataLoadedException, InvalidAttributeException, NonNumericAttributeException
)
from repository.penguin_repo import PenguinRepo
from repository.penguin_repo_file import PenguinRepoFile
from service.penguin_service import PenguinService


class TestPenguinServiceFilter(unittest.TestCase):
    """Test cases for filter functionality
    
    Time Complexity: O(n) where n is the number of penguins
    Space Complexity: O(k) where k is the number of matching penguins
    """

    def setUp(self):
        """Set up test fixtures"""
        self.repo = PenguinRepo()
        self.file_repo = PenguinRepoFile("test_data")
        self.service = PenguinService(self.repo, self.file_repo)
        
        # Add sample penguins
        penguins = [
            Penguin("Adelie", 181.0, 39.1, 18.7, 3750.0, "Torgersen", "MALE"),
            Penguin("Adelie", 186.0, 39.5, 17.4, 3800.0, "Torgersen", "FEMALE"),
            Penguin("Gentoo", 217.0, 46.1, 13.2, 4950.0, "Biscoe", "FEMALE"),
            Penguin("Gentoo", 230.0, 49.6, 16.0, 5700.0, "Biscoe", "MALE"),
            Penguin("Chinstrap", 195.0, 49.0, 19.5, 3950.0, "Dream", "MALE"),
        ]
        self.repo.add_all(penguins)

    def test_filter_no_data_loaded(self):
        """Test filter raises exception when no data loaded"""
        empty_service = PenguinService(PenguinRepo(), self.file_repo)
        
        with self.assertRaises(NoDataLoadedException):
            empty_service.filter_data('species', 'Adelie')

    def test_filter_invalid_attribute(self):
        """Test filter raises exception for invalid attribute"""
        with self.assertRaises(InvalidAttributeException):
            self.service.filter_data('invalid_attr', 'value')

    def test_filter_numeric_greater(self):
        """Test filtering numeric attribute (greater than)"""
        # Filter body_mass_g > 4000
        result = self.service.filter_data('body_mass_g', '4000')
        
        self.assertEqual(len(result), 2)
        for penguin in result:
            self.assertGreater(penguin.get_body_mass_g(), 4000)

    def test_filter_string_equal(self):
        """Test filtering string attribute (equal)"""
        # Filter species == 'Adelie'
        result = self.service.filter_data('species', 'Adelie')
        
        self.assertEqual(len(result), 2)
        for penguin in result:
            self.assertEqual(penguin.get_species(), 'Adelie')

    def test_filter_no_match(self):
        """Test filter returns empty list when no matches"""
        result = self.service.filter_data('body_mass_g', '10000')
        
        self.assertEqual(len(result), 0)


class TestPenguinServiceDescribe(unittest.TestCase):
    """Test cases for describe functionality
    
    Time Complexity: O(n) where n is the number of penguins
    Space Complexity: O(1) - only stores min, max, sum, count
    """

    def setUp(self):
        """Set up test fixtures"""
        self.repo = PenguinRepo()
        self.file_repo = PenguinRepoFile("test_data")
        self.service = PenguinService(self.repo, self.file_repo)
        
        # Add sample penguins with known values
        penguins = [
            Penguin("Adelie", 180.0, 40.0, 18.0, 3000.0, "Torgersen", "MALE"),
            Penguin("Adelie", 190.0, 42.0, 19.0, 4000.0, "Torgersen", "FEMALE"),
            Penguin("Adelie", 200.0, 44.0, 20.0, 5000.0, "Torgersen", "MALE"),
        ]
        self.repo.add_all(penguins)

    def test_describe_no_data_loaded(self):
        """Test describe raises exception when no data loaded"""
        empty_service = PenguinService(PenguinRepo(), self.file_repo)
        
        with self.assertRaises(NoDataLoadedException):
            empty_service.describe_attribute('body_mass_g')

    def test_describe_invalid_attribute(self):
        """Test describe raises exception for invalid attribute"""
        with self.assertRaises(InvalidAttributeException):
            self.service.describe_attribute('invalid_attr')

    def test_describe_non_numeric_attribute(self):
        """Test describe raises exception for non-numeric attribute"""
        with self.assertRaises(NonNumericAttributeException):
            self.service.describe_attribute('species')

    def test_describe_calculates_min(self):
        """Test describe correctly calculates minimum"""
        stats = self.service.describe_attribute('body_mass_g')
        
        self.assertEqual(stats['min'], 3000.0)

    def test_describe_calculates_max(self):
        """Test describe correctly calculates maximum"""
        stats = self.service.describe_attribute('body_mass_g')
        
        self.assertEqual(stats['max'], 5000.0)

    def test_describe_calculates_mean(self):
        """Test describe correctly calculates mean"""
        stats = self.service.describe_attribute('body_mass_g')
        
        # Mean of 3000, 4000, 5000 = 4000
        self.assertEqual(stats['mean'], 4000.0)

    def test_describe_flipper_length(self):
        """Test describe for flipper_length_mm"""
        stats = self.service.describe_attribute('flipper_length_mm')
        
        self.assertEqual(stats['min'], 180.0)
        self.assertEqual(stats['max'], 200.0)
        self.assertEqual(stats['mean'], 190.0)


class TestPenguinServiceUnique(unittest.TestCase):
    """Test cases for unique functionality
    
    Time Complexity: O(n) where n is the number of penguins
    Space Complexity: O(k) where k is the number of unique values
    """

    def setUp(self):
        """Set up test fixtures"""
        self.repo = PenguinRepo()
        self.file_repo = PenguinRepoFile("test_data")
        self.service = PenguinService(self.repo, self.file_repo)
        
        # Add sample penguins
        penguins = [
            Penguin("Adelie", 181.0, 39.1, 18.7, 3750.0, "Torgersen", "MALE"),
            Penguin("Adelie", 186.0, 39.5, 17.4, 3800.0, "Torgersen", "FEMALE"),
            Penguin("Adelie", 195.0, 40.0, 18.0, 3900.0, "Dream", "MALE"),
            Penguin("Gentoo", 217.0, 46.1, 13.2, 4950.0, "Biscoe", "FEMALE"),
            Penguin("Chinstrap", 195.0, 49.0, 19.5, 3950.0, "Dream", "MALE"),
        ]
        self.repo.add_all(penguins)

    def test_unique_no_data_loaded(self):
        """Test unique raises exception when no data loaded"""
        empty_service = PenguinService(PenguinRepo(), self.file_repo)
        
        with self.assertRaises(NoDataLoadedException):
            empty_service.unique_values('species')

    def test_unique_invalid_attribute(self):
        """Test unique raises exception for invalid attribute"""
        with self.assertRaises(InvalidAttributeException):
            self.service.unique_values('invalid_attr')

    def test_unique_species(self):
        """Test unique correctly counts species"""
        unique = self.service.unique_values('species')
        
        self.assertEqual(unique['Adelie'], 3)
        self.assertEqual(unique['Gentoo'], 1)
        self.assertEqual(unique['Chinstrap'], 1)

    def test_unique_island(self):
        """Test unique correctly counts islands"""
        unique = self.service.unique_values('island')
        
        self.assertEqual(unique['Torgersen'], 2)
        self.assertEqual(unique['Dream'], 2)
        self.assertEqual(unique['Biscoe'], 1)

    def test_unique_sex(self):
        """Test unique correctly counts sex"""
        unique = self.service.unique_values('sex')
        
        self.assertEqual(unique['MALE'], 3)
        self.assertEqual(unique['FEMALE'], 2)

    def test_unique_returns_all_values(self):
        """Test unique returns all unique values"""
        unique = self.service.unique_values('species')
        
        self.assertEqual(len(unique), 3)
        self.assertIn('Adelie', unique)
        self.assertIn('Gentoo', unique)
        self.assertIn('Chinstrap', unique)


class TestPenguinServiceSort(unittest.TestCase):
    """Test cases for sort functionality"""

    def setUp(self):
        """Set up test fixtures"""
        self.repo = PenguinRepo()
        self.file_repo = PenguinRepoFile("test_data")
        self.service = PenguinService(self.repo, self.file_repo)
        
        penguins = [
            Penguin("Adelie", 181.0, 39.1, 18.7, 3750.0, "Torgersen", "MALE"),
            Penguin("Gentoo", 230.0, 49.6, 16.0, 5700.0, "Biscoe", "MALE"),
            Penguin("Chinstrap", 195.0, 49.0, 19.5, 3950.0, "Dream", "MALE"),
        ]
        self.repo.add_all(penguins)

    def test_sort_ascending(self):
        """Test sorting in ascending order"""
        sorted_penguins = self.service.sort_data('body_mass_g', 'asc')
        
        for i in range(len(sorted_penguins) - 1):
            self.assertLessEqual(
                sorted_penguins[i].get_body_mass_g(),
                sorted_penguins[i+1].get_body_mass_g()
            )

    def test_sort_descending(self):
        """Test sorting in descending order"""
        sorted_penguins = self.service.sort_data('body_mass_g', 'desc')
        
        for i in range(len(sorted_penguins) - 1):
            self.assertGreaterEqual(
                sorted_penguins[i].get_body_mass_g(),
                sorted_penguins[i+1].get_body_mass_g()
            )


class TestSaveRandomFunctionality(unittest.TestCase):
    """Test cases for save_random functionality
    
    Time Complexity: O(k) for random selection
    Space Complexity: O(k) for storing selected penguins
    """
    
    def setUp(self):
        """Set up test fixtures"""
        import os
        self.repo = PenguinRepo()
        self.file_repo = PenguinRepoFile("test_data")
        self.service = PenguinService(self.repo, self.file_repo)
        
        # Create test_data directory if it doesn't exist
        os.makedirs("test_data", exist_ok=True)
        
        # Add test penguins
        penguins = [
            Penguin("Adelie", 181.0, 39.1, 18.7, 3750.0, "Torgersen", "MALE"),
            Penguin("Adelie", 186.0, 39.5, 17.4, 3800.0, "Torgersen", "FEMALE"),
            Penguin("Gentoo", 211.0, 46.1, 13.2, 4500.0, "Biscoe", "FEMALE"),
            Penguin("Gentoo", 230.0, 49.9, 16.1, 5200.0, "Biscoe", "MALE"),
            Penguin("Chinstrap", 195.0, 46.5, 17.9, 3500.0, "Dream", "FEMALE"),
        ]
        self.repo.add_all(penguins)
    
    def tearDown(self):
        """Clean up test files"""
        import os
        for f in ["test_data/test_random.csv", "test_data/test_random_all.csv", 
                  "test_data/test_random_one.csv"]:
            try:
                os.remove(f)
            except:
                pass
    
    def test_save_random_valid_k(self):
        """Test saving k random penguins"""
        result = self.service.save_random(3, "test_random.csv")
        self.assertEqual(len(result), 3)
    
    def test_save_random_all_penguins(self):
        """Test saving all penguins"""
        result = self.service.save_random(5, "test_random_all.csv")
        self.assertEqual(len(result), 5)
    
    def test_save_random_single_penguin(self):
        """Test saving single penguin"""
        result = self.service.save_random(1, "test_random_one.csv")
        self.assertEqual(len(result), 1)
    
    def test_save_random_k_zero(self):
        """Test save_random with k=0"""
        with self.assertRaises(ValueError):
            self.service.save_random(0, "test.csv")
    
    def test_save_random_k_negative(self):
        """Test save_random with negative k"""
        with self.assertRaises(ValueError):
            self.service.save_random(-1, "test.csv")
    
    def test_save_random_k_too_large(self):
        """Test save_random with k > number of penguins"""
        with self.assertRaises(ValueError):
            self.service.save_random(10, "test.csv")
    
    def test_save_random_no_data_loaded(self):
        """Test save_random raises exception when no data loaded"""
        empty_service = PenguinService(PenguinRepo(), self.file_repo)
        with self.assertRaises(NoDataLoadedException):
            empty_service.save_random(3, "test.csv")


class TestGenerateResearchGroups(unittest.TestCase):
    """Test cases for generate_research_groups functionality
    
    Time Complexity: O(C(n,k)) where C(n,k) is combinations
    Space Complexity: O(C(n,k) * k) for storing valid groups
    """
    
    def setUp(self):
        """Set up test fixtures with small dataset (max 10 penguins)"""
        self.repo = PenguinRepo()
        self.file_repo = PenguinRepoFile("test_data")
        self.service = PenguinService(self.repo, self.file_repo)
        
        # Add exactly 6 penguins (2 of each species)
        penguins = [
            Penguin("Adelie", 181.0, 39.1, 18.7, 3750.0, "Torgersen", "MALE"),
            Penguin("Adelie", 186.0, 39.5, 17.4, 3800.0, "Torgersen", "FEMALE"),
            Penguin("Gentoo", 211.0, 46.1, 13.2, 4500.0, "Biscoe", "FEMALE"),
            Penguin("Gentoo", 230.0, 49.9, 16.1, 5200.0, "Biscoe", "MALE"),
            Penguin("Chinstrap", 195.0, 46.5, 17.9, 3500.0, "Dream", "FEMALE"),
            Penguin("Chinstrap", 200.0, 48.0, 18.5, 3700.0, "Dream", "MALE"),
        ]
        self.repo.add_all(penguins)
    
    def test_generate_groups_k3(self):
        """Test generating groups of size 3"""
        groups = self.service.generate_research_groups(3)
        # Each valid group must have at least one penguin from each species
        for group in groups:
            species = set(p.get_species() for p in group)
            self.assertEqual(len(species), 3)
            self.assertIn("Adelie", species)
            self.assertIn("Gentoo", species)
            self.assertIn("Chinstrap", species)
    
    def test_generate_groups_k4(self):
        """Test generating groups of size 4"""
        groups = self.service.generate_research_groups(4)
        for group in groups:
            self.assertEqual(len(group), 4)
            species = set(p.get_species() for p in group)
            self.assertEqual(len(species), 3)
    
    def test_generate_groups_all_distinct(self):
        """Test that penguins in each group are distinct"""
        groups = self.service.generate_research_groups(3)
        for group in groups:
            penguin_ids = [id(p) for p in group]
            self.assertEqual(len(penguin_ids), len(set(penguin_ids)))
    
    def test_generate_groups_k_less_than_3(self):
        """Test that k < 3 raises error"""
        with self.assertRaises(ValueError):
            self.service.generate_research_groups(2)
    
    def test_generate_groups_k_too_large(self):
        """Test that k > n raises error"""
        with self.assertRaises(ValueError):
            self.service.generate_research_groups(10)
    
    def test_generate_groups_no_data(self):
        """Test with no data loaded"""
        empty_service = PenguinService(PenguinRepo(), self.file_repo)
        with self.assertRaises(NoDataLoadedException):
            empty_service.generate_research_groups(3)


class TestSplitIntoGroups(unittest.TestCase):
    """Test cases for split_into_groups functionality
    
    Time Complexity: O(2^n) for generating all possible splits
    Space Complexity: O(2^n) for storing valid splits
    """
    
    def setUp(self):
        """Set up test fixtures with small dataset"""
        self.repo = PenguinRepo()
        self.file_repo = PenguinRepoFile("test_data")
        self.service = PenguinService(self.repo, self.file_repo)
        
        # Add 4 penguins with known body masses
        penguins = [
            Penguin("Adelie", 181.0, 39.1, 18.7, 3000.0, "Torgersen", "MALE"),
            Penguin("Adelie", 186.0, 39.5, 17.4, 3000.0, "Torgersen", "FEMALE"),
            Penguin("Gentoo", 211.0, 46.1, 13.2, 4000.0, "Biscoe", "FEMALE"),
            Penguin("Chinstrap", 195.0, 46.5, 17.9, 4000.0, "Dream", "FEMALE"),
        ]
        self.repo.add_all(penguins)
    
    def test_split_valid_threshold(self):
        """Test splitting with valid threshold"""
        # Total mass = 14000g, threshold of 8000 should allow splits
        splits = self.service.split_into_groups(8000)
        for g1, g2 in splits:
            self.assertGreaterEqual(len(g1), 2)
            self.assertGreaterEqual(len(g2), 2)
            mass1 = sum(p.get_body_mass_g() for p in g1)
            mass2 = sum(p.get_body_mass_g() for p in g2)
            self.assertLessEqual(mass1, 8000)
            self.assertLessEqual(mass2, 8000)
    
    def test_split_each_group_has_two(self):
        """Test that each group has at least 2 penguins"""
        splits = self.service.split_into_groups(10000)
        for g1, g2 in splits:
            self.assertGreaterEqual(len(g1), 2)
            self.assertGreaterEqual(len(g2), 2)
    
    def test_split_threshold_too_low(self):
        """Test that too low threshold returns no splits"""
        # With 4 penguins of 3000-4000g each, threshold of 5000 won't work
        splits = self.service.split_into_groups(5000)
        self.assertEqual(len(splits), 0)
    
    def test_split_all_penguins_assigned(self):
        """Test that all penguins are assigned to groups"""
        splits = self.service.split_into_groups(20000)
        for g1, g2 in splits:
            total = len(g1) + len(g2)
            self.assertEqual(total, 4)
    
    def test_split_too_few_penguins(self):
        """Test that < 4 penguins raises error"""
        small_repo = PenguinRepo()
        small_service = PenguinService(small_repo, self.file_repo)
        small_repo.add_penguin(Penguin("Adelie", 180.0, 40.0, 18.0, 3000.0, "Dream", "MALE"))
        small_repo.add_penguin(Penguin("Adelie", 180.0, 40.0, 18.0, 3000.0, "Dream", "MALE"))
        small_repo.add_penguin(Penguin("Adelie", 180.0, 40.0, 18.0, 3000.0, "Dream", "MALE"))
        with self.assertRaises(ValueError):
            small_service.split_into_groups(10000)
    
    def test_split_no_data(self):
        """Test with no data loaded"""
        empty_service = PenguinService(PenguinRepo(), self.file_repo)
        with self.assertRaises(NoDataLoadedException):
            empty_service.split_into_groups(10000)


class TestComplexityDocumentation(unittest.TestCase):
    """Verify that time and space complexity is documented for all methods"""
    
    def test_filter_complexity_documented(self):
        """Verify filter has complexity documentation"""
        docstring = PenguinService.filter_data.__doc__
        self.assertIn("Time Complexity", docstring)
        self.assertIn("Space Complexity", docstring)
    
    def test_describe_complexity_documented(self):
        """Verify describe has complexity documentation"""
        docstring = PenguinService.describe_attribute.__doc__
        self.assertIn("Time Complexity", docstring)
        self.assertIn("Space Complexity", docstring)
    
    def test_unique_complexity_documented(self):
        """Verify unique has complexity documentation"""
        docstring = PenguinService.unique_values.__doc__
        self.assertIn("Time Complexity", docstring)
        self.assertIn("Space Complexity", docstring)
    
    def test_sort_complexity_documented(self):
        """Verify sort has complexity documentation"""
        docstring = PenguinService.sort_data.__doc__
        self.assertIn("Time Complexity", docstring)
        self.assertIn("Space Complexity", docstring)
    
    def test_save_random_complexity_documented(self):
        """Verify save_random has complexity documentation"""
        docstring = PenguinService.save_random.__doc__
        self.assertIn("Time Complexity", docstring)
        self.assertIn("Space Complexity", docstring)
    
    def test_generate_research_groups_complexity_documented(self):
        """Verify generate_research_groups has complexity documentation"""
        docstring = PenguinService.generate_research_groups.__doc__
        self.assertIn("Time Complexity", docstring)
        self.assertIn("Space Complexity", docstring)
    
    def test_split_into_groups_complexity_documented(self):
        """Verify split_into_groups has complexity documentation"""
        docstring = PenguinService.split_into_groups.__doc__
        self.assertIn("Time Complexity", docstring)
        self.assertIn("Space Complexity", docstring)


if __name__ == '__main__':
    unittest.main()
