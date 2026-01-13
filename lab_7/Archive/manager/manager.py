import copy
from domain.MyString import MyString


class MyStringManager:
    """
    Manager class for handling a collection of MyString objects.
    Provides operations like add, delete, search, filter, and undo functionality.
    """
    
    def __init__(self):
        """Initialize the manager with empty string list and undo history."""
        self.__string_list = []
        self.__undo_list = []
    
    @property
    def string_list(self):
        """Get the current list of MyString objects."""
        return self.__string_list
    
    @property
    def undo_list(self):
        """Get the undo history list."""
        return self.__undo_list
    
    @string_list.setter
    def string_list(self, new_list):
        """Set the current list of MyString objects."""
        self.__string_list = new_list
    
    @undo_list.setter
    def undo_list(self, new_list):
        """Set the undo history list."""
        self.__undo_list = new_list
    
    def add_to_string_list(self, my_string: MyString):
        """
        Add a MyString object to the current list.
        :param my_string: the MyString to add
        :return: None
        """
        self.__string_list.append(my_string)
    
    def add_to_undo_list(self, lst: list):
        """
        Add a snapshot of the list to undo history using deep copy.
        :param lst: the list to save in history
        :return: None
        """
        self.__undo_list.append(copy.deepcopy(lst))
    
    def add_string(self, my_string: MyString):
        """
        Add a MyString to the string list with undo support.
        :param my_string: the MyString to add
        :return: None
        """
        # Save current state to undo list
        self.add_to_undo_list(self.__string_list)
        # Add string to current list
        self.add_to_string_list(my_string)
    
    def add_default_strings(self):
        """
        Add default MyString objects to the list for demonstration purposes.
        :return: None
        """
        self.add_string(MyString('hello'))
        self.add_string(MyString('world'))
        self.add_string(MyString('python'))
        self.add_string(MyString('test'))
    
    def search_by_content(self, content: str):
        """
        Search for a MyString by its content.
        :param content: the string content to search for
        :return: the MyString if found, None otherwise
        """
        for my_string in self.__string_list:
            if my_string.to_str() == content:
                return my_string
        return None
    
    def delete_by_content(self, content: str):
        """
        Delete a MyString by its content.
        :param content: the string content to delete
        :return: the deleted MyString if found, None otherwise
        """
        # Save current state to undo list
        self.add_to_undo_list(self.string_list)
        for my_string in self.string_list:
            if my_string.to_str() == content:
                self.string_list.remove(my_string)
                return my_string
        return None
    
    def remove_strings_containing(self, substring: str):
        """
        Remove all MyString objects that contain the given substring.
        :param substring: the substring to search for
        :return: None
        """
        self.add_to_undo_list(self.string_list)
        string_list = self.string_list
        i = 0
        while i < len(string_list):
            if string_list[i].find(substring) != -1:
                string_list.pop(i)
            else:
                i += 1
    
    def filter_by_length(self, min_length: int, max_length: int) -> list:
        """
        Get all MyString objects with length between min_length and max_length (inclusive).
        :param min_length: minimum length
        :param max_length: maximum length
        :return: a list with the found MyString objects
        """
        found_strings = []
        for my_string in self.string_list:
            if min_length <= len(my_string) <= max_length:
                found_strings.append(my_string)
        return found_strings
    
    def filter_by_first_character(self, char: str) -> list:
        """
        Get all MyString objects that start with the given character.
        :param char: the character to filter by
        :return: a list with the found MyString objects
        """
        if not char.islower() or not char.isalpha() or len(char) != 1:
            raise TypeError("Must be a single lowercase letter")
        
        found_strings = []
        for my_string in self.string_list:
            if len(my_string) > 0 and my_string[0] == char:
                found_strings.append(my_string)
        return found_strings
    
    def concatenate_all(self) -> MyString:
        """
        Concatenate all MyString objects in the list.
        :return: a new MyString containing all strings concatenated
        """
        if len(self.string_list) == 0:
            return MyString('')
        
        result = self.string_list[0]
        for i in range(1, len(self.string_list)):
            result = result + self.string_list[i]
        return result
    
    def modify_string_at_index(self, string_index: int, char_index: int, new_char: str):
        """
        Modify a character at a specific position in a MyString at given index.
        :param string_index: index of the MyString in the list
        :param char_index: index of the character to modify
        :param new_char: the new character
        :return: None
        :raises: IndexError if string_index is out of bounds
        :raises: TypeError if new_char is invalid
        """
        if string_index < 0 or string_index >= len(self.string_list):
            raise IndexError("String index out of range")
        
        # Save current state to undo list
        self.add_to_undo_list(self.string_list)
        # Modify the character
        self.string_list[string_index][char_index] = new_char
    
    def rotate_string_at_index(self, string_index: int, positions: int):
        """
        Rotate a MyString at given index by specified positions.
        :param string_index: index of the MyString in the list
        :param positions: number of positions to rotate
        :return: None
        :raises: IndexError if string_index is out of bounds
        """
        if string_index < 0 or string_index >= len(self.string_list):
            raise IndexError("String index out of range")
        
        # Save current state to undo list
        self.add_to_undo_list(self.string_list)
        # Rotate the string
        self.string_list[string_index].rotate(positions)
    
    def insert_character_at_index(self, string_index: int, position: int, char: str):
        """
        Insert a character at a specific position in a MyString at given index.
        :param string_index: index of the MyString in the list
        :param position: position where to insert the character
        :param char: the character to insert
        :return: None
        :raises: IndexError if string_index is out of bounds
        """
        if string_index < 0 or string_index >= len(self.string_list):
            raise IndexError("String index out of range")
        
        # Save current state to undo list
        self.add_to_undo_list(self.string_list)
        # Insert the character
        self.string_list[string_index].insert(position, char)
    
    def remove_character_from_string(self, string_index: int, char: str, start=0, end=None):
        """
        Remove all occurrences of a character from a MyString at given index.
        :param string_index: index of the MyString in the list
        :param char: the character to remove
        :param start: start position for removal (default: 0)
        :param end: end position for removal (default: None)
        :return: None
        :raises: IndexError if string_index is out of bounds
        :raises: ValueError if character not found
        """
        if string_index < 0 or string_index >= len(self.string_list):
            raise IndexError("String index out of range")
        
        # Save current state to undo list
        self.add_to_undo_list(self.string_list)
        # Remove the character
        self.string_list[string_index].remove_character(char, start, end)
    
    def replace_in_string(self, string_index: int, old: str, new: str, count=None):
        """
        Replace occurrences of a substring in a MyString at given index.
        :param string_index: index of the MyString in the list
        :param old: the substring to replace
        :param new: the replacement substring
        :param count: number of occurrences to replace (default: None - all)
        :return: None
        :raises: IndexError if string_index is out of bounds
        """
        if string_index < 0 or string_index >= len(self.string_list):
            raise IndexError("String index out of range")
        
        # Save current state to undo list
        self.add_to_undo_list(self.string_list)
        # Replace the substring
        self.string_list[string_index].replace(old, new, count)
    
    def undo(self):
        """
        Restore the list to the previous state from undo history.
        :return: None
        :raises: ValueError if there is nothing to undo
        """
        if len(self.undo_list) == 0:
            raise ValueError("Nothing in history")
        last_elem_history = self.undo_list.pop()
        self.string_list = last_elem_history
    
    def get_all_strings_as_list(self) -> list:
        """
        Get all MyString objects as a list of their string representations.
        :return: list of strings
        """
        return [s.to_str() for s in self.string_list]
    
    def clear_all(self):
        """
        Clear all MyString objects from the list (with undo support).
        :return: None
        """
        self.add_to_undo_list(self.string_list)
        self.string_list = []
    
    def get_total_length(self) -> int:
        """
        Get the total length of all MyString objects combined.
        :return: total length as integer
        """
        return sum(len(s) for s in self.string_list)
    
    def sort_by_length(self, reverse=False):
        """
        Sort the MyString objects by their length.
        :param reverse: if True, sort in descending order
        :return: None
        """
        self.add_to_undo_list(self.string_list)
        self.string_list.sort(key=lambda s: len(s), reverse=reverse)
    
    def count_strings(self) -> int:
        """
        Get the number of MyString objects in the list.
        :return: count as integer
        """
        return len(self.string_list)
