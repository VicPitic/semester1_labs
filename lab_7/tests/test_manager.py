import unittest
import sys
from pathlib import Path

# Add parent directory to path to import modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from domain.MyString import MyString
from manager.manager import MyStringManager


class TestMyStringManager(unittest.TestCase):
    """Test cases for MyStringManager class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.manager = MyStringManager()
    
    def test_init(self):
        """Test manager initialization."""
        self.assertEqual(len(self.manager.string_list), 0)
        self.assertEqual(len(self.manager.undo_list), 0)
    
    def test_add_string(self):
        """Test adding a string to the manager."""
        my_str = MyString('hello')
        self.manager.add_string(my_str)
        
        self.assertEqual(len(self.manager.string_list), 1)
        self.assertEqual(self.manager.string_list[0].to_str(), 'hello')
        # Check that undo list has the previous state (empty list)
        self.assertEqual(len(self.manager.undo_list), 1)
        self.assertEqual(len(self.manager.undo_list[0]), 0)
    
    def test_add_multiple_strings(self):
        """Test adding multiple strings."""
        self.manager.add_string(MyString('hello'))
        self.manager.add_string(MyString('world'))
        self.manager.add_string(MyString('python'))
        
        self.assertEqual(len(self.manager.string_list), 3)
        self.assertEqual(self.manager.string_list[0].to_str(), 'hello')
        self.assertEqual(self.manager.string_list[1].to_str(), 'world')
        self.assertEqual(self.manager.string_list[2].to_str(), 'python')
    
    def test_add_default_strings(self):
        """Test adding default strings."""
        self.manager.add_default_strings()
        
        self.assertEqual(len(self.manager.string_list), 4)
        self.assertEqual(self.manager.string_list[0].to_str(), 'hello')
        self.assertEqual(self.manager.string_list[1].to_str(), 'world')
        self.assertEqual(self.manager.string_list[2].to_str(), 'python')
        self.assertEqual(self.manager.string_list[3].to_str(), 'test')
    
    def test_search_by_content_found(self):
        """Test searching for an existing string."""
        self.manager.add_string(MyString('hello'))
        self.manager.add_string(MyString('world'))
        
        result = self.manager.search_by_content('world')
        self.assertIsNotNone(result)
        self.assertEqual(result.to_str(), 'world')
    
    def test_search_by_content_not_found(self):
        """Test searching for a non-existing string."""
        self.manager.add_string(MyString('hello'))
        
        result = self.manager.search_by_content('python')
        self.assertIsNone(result)
    
    def test_search_empty_list(self):
        """Test searching in an empty list."""
        result = self.manager.search_by_content('hello')
        self.assertIsNone(result)
    
    def test_delete_by_content_found(self):
        """Test deleting an existing string."""
        self.manager.add_string(MyString('hello'))
        self.manager.add_string(MyString('world'))
        self.manager.add_string(MyString('python'))
        
        deleted = self.manager.delete_by_content('world')
        
        self.assertIsNotNone(deleted)
        self.assertEqual(deleted.to_str(), 'world')
        self.assertEqual(len(self.manager.string_list), 2)
        self.assertEqual(self.manager.string_list[0].to_str(), 'hello')
        self.assertEqual(self.manager.string_list[1].to_str(), 'python')
    
    def test_delete_by_content_not_found(self):
        """Test deleting a non-existing string."""
        self.manager.add_string(MyString('hello'))
        
        deleted = self.manager.delete_by_content('world')
        
        self.assertIsNone(deleted)
        self.assertEqual(len(self.manager.string_list), 1)
    
    def test_remove_strings_containing(self):
        """Test removing strings containing a substring."""
        self.manager.add_string(MyString('hello'))
        self.manager.add_string(MyString('world'))
        self.manager.add_string(MyString('help'))
        self.manager.add_string(MyString('python'))
        
        self.manager.remove_strings_containing('hel')
        
        self.assertEqual(len(self.manager.string_list), 2)
        self.assertEqual(self.manager.string_list[0].to_str(), 'world')
        self.assertEqual(self.manager.string_list[1].to_str(), 'python')
    
    def test_remove_strings_containing_not_found(self):
        """Test removing strings with substring not in any string."""
        self.manager.add_string(MyString('hello'))
        self.manager.add_string(MyString('world'))
        
        self.manager.remove_strings_containing('xyz')
        
        self.assertEqual(len(self.manager.string_list), 2)
    
    def test_filter_by_length(self):
        """Test filtering strings by length."""
        self.manager.add_string(MyString('hi'))       # length 2
        self.manager.add_string(MyString('hello'))    # length 5
        self.manager.add_string(MyString('world'))    # length 5
        self.manager.add_string(MyString('python'))   # length 6
        self.manager.add_string(MyString('a'))        # length 1
        
        result = self.manager.filter_by_length(4, 5)
        
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].to_str(), 'hello')
        self.assertEqual(result[1].to_str(), 'world')
    
    def test_filter_by_length_no_matches(self):
        """Test filtering with no matches."""
        self.manager.add_string(MyString('hi'))
        self.manager.add_string(MyString('bye'))
        
        result = self.manager.filter_by_length(10, 15)
        
        self.assertEqual(len(result), 0)
    
    def test_modify_string_at_index(self):
        """Test modifying a character in a string at a given index."""
        self.manager.add_string(MyString('hello'))
        self.manager.add_string(MyString('world'))
        
        self.manager.modify_string_at_index(1, 0, 'c')
        
        self.assertEqual(self.manager.string_list[1].to_str(), 'corld')
    
    def test_modify_string_at_index_invalid(self):
        """Test modifying with invalid index."""
        self.manager.add_string(MyString('hello'))
        
        with self.assertRaises(IndexError):
            self.manager.modify_string_at_index(5, 0, 'a')
    
    def test_concatenate_all(self):
        """Test concatenating all strings."""
        self.manager.add_string(MyString('hello'))
        self.manager.add_string(MyString('world'))
        self.manager.add_string(MyString('python'))
        
        result = self.manager.concatenate_all()
        
        self.assertEqual(result.to_str(), 'helloworldpython')
    
    def test_concatenate_all_empty_list(self):
        """Test concatenating an empty list."""
        result = self.manager.concatenate_all()
        
        self.assertEqual(result.to_str(), '')
    
    def test_concatenate_all_single_string(self):
        """Test concatenating a single string."""
        self.manager.add_string(MyString('hello'))
        
        result = self.manager.concatenate_all()
        
        self.assertEqual(result.to_str(), 'hello')
    
    def test_rotate_string_at_index(self):
        """Test rotating a string at a given index."""
        self.manager.add_string(MyString('hello'))
        self.manager.add_string(MyString('world'))
        
        self.manager.rotate_string_at_index(0, 2)
        
        self.assertEqual(self.manager.string_list[0].to_str(), 'lohel')
    
    def test_rotate_string_at_index_invalid(self):
        """Test rotating with invalid index."""
        self.manager.add_string(MyString('hello'))
        
        with self.assertRaises(IndexError):
            self.manager.rotate_string_at_index(5, 2)
    
    def test_undo_after_add(self):
        """Test undo after adding a string."""
        self.manager.add_string(MyString('hello'))
        self.manager.add_string(MyString('world'))
        
        self.assertEqual(len(self.manager.string_list), 2)
        
        self.manager.undo()
        
        self.assertEqual(len(self.manager.string_list), 1)
        self.assertEqual(self.manager.string_list[0].to_str(), 'hello')
    
    def test_undo_after_delete(self):
        """Test undo after deleting a string."""
        self.manager.add_string(MyString('hello'))
        self.manager.add_string(MyString('world'))
        self.manager.delete_by_content('hello')
        
        self.assertEqual(len(self.manager.string_list), 1)
        
        self.manager.undo()
        
        self.assertEqual(len(self.manager.string_list), 2)
        self.assertEqual(self.manager.string_list[0].to_str(), 'hello')
        self.assertEqual(self.manager.string_list[1].to_str(), 'world')
    
    def test_undo_after_modify(self):
        """Test undo after modifying a string."""
        self.manager.add_string(MyString('hello'))
        original_content = self.manager.string_list[0].to_str()
        
        self.manager.modify_string_at_index(0, 0, 'y')
        
        self.assertEqual(self.manager.string_list[0].to_str(), 'yello')
        
        self.manager.undo()
        
        self.assertEqual(self.manager.string_list[0].to_str(), original_content)
    
    def test_undo_multiple_operations(self):
        """Test multiple undo operations."""
        self.manager.add_string(MyString('hello'))
        self.manager.add_string(MyString('world'))
        self.manager.add_string(MyString('python'))
        
        self.assertEqual(len(self.manager.string_list), 3)
        
        self.manager.undo()
        self.assertEqual(len(self.manager.string_list), 2)
        
        self.manager.undo()
        self.assertEqual(len(self.manager.string_list), 1)
        
        self.manager.undo()
        self.assertEqual(len(self.manager.string_list), 0)
    
    def test_undo_empty_history(self):
        """Test undo with empty history."""
        with self.assertRaises(ValueError) as context:
            self.manager.undo()
        
        self.assertEqual(str(context.exception), "Nothing in history")
    
    def test_undo_preserves_independence(self):
        """Test that undo creates independent copies."""
        self.manager.add_string(MyString('hello'))
        self.manager.add_string(MyString('world'))
        
        # Modify the current list
        self.manager.modify_string_at_index(0, 0, 'y')
        
        # Undo should restore the original state
        self.manager.undo()
        
        # The first string should be 'hello' again
        self.assertEqual(self.manager.string_list[0].to_str(), 'hello')
    
    def test_remove_strings_containing_with_undo(self):
        """Test removing strings containing substring with undo."""
        self.manager.add_string(MyString('hello'))
        self.manager.add_string(MyString('help'))
        self.manager.add_string(MyString('world'))
        
        self.manager.remove_strings_containing('hel')
        
        self.assertEqual(len(self.manager.string_list), 1)
        self.assertEqual(self.manager.string_list[0].to_str(), 'world')
        
        self.manager.undo()
        
        self.assertEqual(len(self.manager.string_list), 3)
    
    def test_rotate_string_at_index_with_undo(self):
        """Test rotating string with undo."""
        self.manager.add_string(MyString('hello'))
        
        self.manager.rotate_string_at_index(0, 2)
        self.assertEqual(self.manager.string_list[0].to_str(), 'lohel')
        
        self.manager.undo()
        self.assertEqual(self.manager.string_list[0].to_str(), 'hello')


if __name__ == '__main__':
    unittest.main()
