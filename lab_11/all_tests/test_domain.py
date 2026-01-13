"""
Tests for Domain layer - Penguin class
"""
import unittest
from domain.penguin import Penguin
from domain.validation import PenguinValidator
from domain.exceptions import ValidationException


class TestPenguin(unittest.TestCase):
    """Test cases for Penguin entity"""

    def test_create_penguin(self):
        """Test penguin creation with valid data"""
        penguin = Penguin("Adelie", 181.0, 39.1, 18.7, 3750.0, "Torgersen", "MALE")
        
        self.assertEqual(penguin.get_species(), "Adelie")
        self.assertEqual(penguin.get_flipper_length_mm(), 181.0)
        self.assertEqual(penguin.get_culmen_length_mm(), 39.1)
        self.assertEqual(penguin.get_culmen_depth_mm(), 18.7)
        self.assertEqual(penguin.get_body_mass_g(), 3750.0)
        self.assertEqual(penguin.get_island(), "Torgersen")
        self.assertEqual(penguin.get_sex(), "MALE")

    def test_penguin_setters(self):
        """Test penguin setters"""
        penguin = Penguin("Adelie", 181.0, 39.1, 18.7, 3750.0, "Torgersen", "MALE")
        
        penguin.set_species("Chinstrap")
        self.assertEqual(penguin.get_species(), "Chinstrap")
        
        penguin.set_flipper_length_mm(195.0)
        self.assertEqual(penguin.get_flipper_length_mm(), 195.0)
        
        penguin.set_body_mass_g(4200.0)
        self.assertEqual(penguin.get_body_mass_g(), 4200.0)

    def test_penguin_get_attribute(self):
        """Test getting attribute by name"""
        penguin = Penguin("Gentoo", 220.0, 47.5, 15.0, 5500.0, "Biscoe", "FEMALE")
        
        self.assertEqual(penguin.get_attribute('species'), "Gentoo")
        self.assertEqual(penguin.get_attribute('flipper_length_mm'), 220.0)
        self.assertEqual(penguin.get_attribute('island'), "Biscoe")

    def test_penguin_get_attribute_invalid(self):
        """Test getting invalid attribute raises error"""
        penguin = Penguin("Adelie", 181.0, 39.1, 18.7, 3750.0, "Torgersen", "MALE")
        
        with self.assertRaises(AttributeError):
            penguin.get_attribute('invalid_attr')

    def test_penguin_to_dict(self):
        """Test converting penguin to dictionary"""
        penguin = Penguin("Adelie", 181.0, 39.1, 18.7, 3750.0, "Torgersen", "MALE")
        d = penguin.to_dict()
        
        self.assertEqual(d['species'], "Adelie")
        self.assertEqual(d['flipper_length_mm'], 181.0)
        self.assertEqual(len(d), 7)

    def test_penguin_equality(self):
        """Test penguin equality comparison"""
        p1 = Penguin("Adelie", 181.0, 39.1, 18.7, 3750.0, "Torgersen", "MALE")
        p2 = Penguin("Adelie", 181.0, 39.1, 18.7, 3750.0, "Torgersen", "MALE")
        p3 = Penguin("Gentoo", 181.0, 39.1, 18.7, 3750.0, "Torgersen", "MALE")
        
        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)

    def test_numeric_attributes(self):
        """Test getting numeric attribute names"""
        numeric_attrs = Penguin.get_numeric_attributes()
        
        self.assertIn('flipper_length_mm', numeric_attrs)
        self.assertIn('culmen_length_mm', numeric_attrs)
        self.assertIn('body_mass_g', numeric_attrs)
        self.assertNotIn('species', numeric_attrs)

    def test_string_attributes(self):
        """Test getting string attribute names"""
        string_attrs = Penguin.get_string_attributes()
        
        self.assertIn('species', string_attrs)
        self.assertIn('island', string_attrs)
        self.assertIn('sex', string_attrs)
        self.assertNotIn('flipper_length_mm', string_attrs)


class TestPenguinValidator(unittest.TestCase):
    """Test cases for PenguinValidator"""

    def setUp(self):
        self.validator = PenguinValidator()

    def test_validate_valid_penguin(self):
        """Test validating a valid penguin"""
        penguin = Penguin("Adelie", 181.0, 39.1, 18.7, 3750.0, "Torgersen", "MALE")
        
        # Should not raise
        self.validator.validate_penguin(penguin)

    def test_validate_invalid_species(self):
        """Test validating penguin with invalid species"""
        penguin = Penguin("InvalidSpecies", 181.0, 39.1, 18.7, 3750.0, "Torgersen", "MALE")
        
        with self.assertRaises(ValidationException):
            self.validator.validate_penguin(penguin)

    def test_validate_invalid_island(self):
        """Test validating penguin with invalid island"""
        penguin = Penguin("Adelie", 181.0, 39.1, 18.7, 3750.0, "InvalidIsland", "MALE")
        
        with self.assertRaises(ValidationException):
            self.validator.validate_penguin(penguin)

    def test_validate_negative_numeric(self):
        """Test validating penguin with negative numeric values"""
        penguin = Penguin("Adelie", -181.0, 39.1, 18.7, 3750.0, "Torgersen", "MALE")
        
        with self.assertRaises(ValidationException):
            self.validator.validate_penguin(penguin)


if __name__ == '__main__':
    unittest.main()
