from domain.MyString import MyString
from manager.manager import MyStringManager


class Console:
    """
    Console UI for managing MyString objects.
    Handles all user interaction and display.
    """
    
    def __init__(self, manager: MyStringManager):
        """
        Initialize the Console with a manager.
        :param manager: MyStringManager instance to manage strings
        """
        self.__manager = manager
    
    @staticmethod
    def print_menu():
        """Display the main menu options."""
        print("\n" + "=" * 60)
        print("MyString Manager - Menu")
        print("=" * 60)
        print("1. Add a new string")
        print("2. Add default strings")
        print("3. Search for a string by content")
        print("4. Delete a string by content")
        print("5. Remove strings containing a substring")
        print("6. Display all strings")
        print("7. Filter strings by length")
        print("8. Filter strings by first character")
        print("9. Concatenate all strings")
        print("10. Modify a character in a string")
        print("11. Rotate a string")
        print("12. Insert character in a string")
        print("13. Remove character from a string")
        print("14. Replace substring in a string")
        print("15. Sort strings by length")
        print("16. Get total length of all strings")
        print("17. Clear all strings")
        print("18. Undo last operation")
        print("x. Exit")
        print("=" * 60)
    
    @staticmethod
    def show_strings(string_list):
        """
        Display a list of MyString objects.
        :param string_list: list of MyString objects to display
        """
        if len(string_list) == 0:
            print("  No strings to display.")
        else:
            for i, my_string in enumerate(string_list):
                print(f"  [{i}] {my_string.to_str()} (length: {len(my_string)})")
    
    def add_string_ui(self):
        """UI for adding a new string."""
        content = input("Enter the string content (lowercase letters only): ").strip()
        try:
            my_string = MyString(content)
            self.__manager.add_string(my_string)
            print(f"✓ String '{content}' added successfully!")
        except TypeError as te:
            print(f"✗ Error: {te}")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def add_default_strings_ui(self):
        """UI for adding default strings."""
        try:
            self.__manager.add_default_strings()
            print(f"✓ Added default strings successfully!")
            print(f"  Current list has {self.__manager.count_strings()} strings.")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def search_string_ui(self):
        """UI for searching a string by content."""
        content = input("Enter the string content to search: ").strip()
        try:
            result = self.__manager.search_by_content(content)
            if result:
                print(f"✓ String found: '{result.to_str()}' (length: {len(result)})")
            else:
                print(f"✗ String '{content}' not found.")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def delete_string_ui(self):
        """UI for deleting a string by content."""
        content = input("Enter the string content to delete: ").strip()
        try:
            deleted = self.__manager.delete_by_content(content)
            if deleted:
                print(f"✓ String '{deleted.to_str()}' deleted successfully!")
                print(f"  Remaining strings: {self.__manager.count_strings()}")
            else:
                print(f"✗ String '{content}' not found.")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def remove_strings_containing_ui(self):
        """UI for removing strings containing a substring."""
        substring = input("Enter the substring to search for: ").strip()
        try:
            count_before = self.__manager.count_strings()
            self.__manager.remove_strings_containing(substring)
            count_after = self.__manager.count_strings()
            removed_count = count_before - count_after
            print(f"✓ Removed {removed_count} string(s) containing '{substring}'.")
            print(f"  Remaining strings: {count_after}")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def display_all_strings_ui(self):
        """UI for displaying all strings."""
        print(f"\nAll strings ({self.__manager.count_strings()} total):")
        Console.show_strings(self.__manager.string_list)
    
    def filter_by_length_ui(self):
        """UI for filtering strings by length."""
        try:
            min_len = int(input("Enter minimum length: ").strip())
            max_len = int(input("Enter maximum length: ").strip())
            
            filtered = self.__manager.filter_by_length(min_len, max_len)
            print(f"\nStrings with length between {min_len} and {max_len} ({len(filtered)} found):")
            Console.show_strings(filtered)
        except ValueError:
            print("✗ Error: Please enter valid numbers.")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def filter_by_first_character_ui(self):
        """UI for filtering strings by first character."""
        char = input("Enter the first character to filter by: ").strip()
        try:
            filtered = self.__manager.filter_by_first_character(char)
            print(f"\nStrings starting with '{char}' ({len(filtered)} found):")
            Console.show_strings(filtered)
        except TypeError as te:
            print(f"✗ Error: {te}")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def concatenate_all_ui(self):
        """UI for concatenating all strings."""
        try:
            result = self.__manager.concatenate_all()
            print(f"✓ Concatenated result: '{result.to_str()}' (length: {len(result)})")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def modify_character_ui(self):
        """UI for modifying a character in a string."""
        try:
            print("\nCurrent strings:")
            Console.show_strings(self.__manager.string_list)
            
            string_idx = int(input("Enter string index: ").strip())
            char_idx = int(input("Enter character index: ").strip())
            new_char = input("Enter new character: ").strip()
            
            old_content = self.__manager.string_list[string_idx].to_str()
            self.__manager.modify_string_at_index(string_idx, char_idx, new_char)
            new_content = self.__manager.string_list[string_idx].to_str()
            
            print(f"✓ Modified successfully!")
            print(f"  Before: '{old_content}'")
            print(f"  After:  '{new_content}'")
        except ValueError:
            print("✗ Error: Please enter valid numbers.")
        except IndexError as ie:
            print(f"✗ Error: {ie}")
        except TypeError as te:
            print(f"✗ Error: {te}")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def rotate_string_ui(self):
        """UI for rotating a string."""
        try:
            print("\nCurrent strings:")
            Console.show_strings(self.__manager.string_list)
            
            string_idx = int(input("Enter string index: ").strip())
            positions = int(input("Enter number of positions to rotate: ").strip())
            
            old_content = self.__manager.string_list[string_idx].to_str()
            self.__manager.rotate_string_at_index(string_idx, positions)
            new_content = self.__manager.string_list[string_idx].to_str()
            
            print(f"✓ Rotated successfully!")
            print(f"  Before: '{old_content}'")
            print(f"  After:  '{new_content}'")
        except ValueError:
            print("✗ Error: Please enter valid numbers.")
        except IndexError as ie:
            print(f"✗ Error: {ie}")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def insert_character_ui(self):
        """UI for inserting a character in a string."""
        try:
            print("\nCurrent strings:")
            Console.show_strings(self.__manager.string_list)
            
            string_idx = int(input("Enter string index: ").strip())
            position = int(input("Enter position to insert at: ").strip())
            char = input("Enter character to insert: ").strip()
            
            old_content = self.__manager.string_list[string_idx].to_str()
            self.__manager.insert_character_at_index(string_idx, position, char)
            new_content = self.__manager.string_list[string_idx].to_str()
            
            print(f"✓ Character inserted successfully!")
            print(f"  Before: '{old_content}'")
            print(f"  After:  '{new_content}'")
        except ValueError:
            print("✗ Error: Please enter valid numbers.")
        except IndexError as ie:
            print(f"✗ Error: {ie}")
        except TypeError as te:
            print(f"✗ Error: {te}")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def remove_character_ui(self):
        """UI for removing a character from a string."""
        try:
            print("\nCurrent strings:")
            Console.show_strings(self.__manager.string_list)
            
            string_idx = int(input("Enter string index: ").strip())
            char = input("Enter character to remove: ").strip()
            
            use_range = input("Specify range? (y/n): ").strip().lower()
            if use_range == 'y':
                start = int(input("Enter start position: ").strip())
                end = int(input("Enter end position: ").strip())
                old_content = self.__manager.string_list[string_idx].to_str()
                self.__manager.remove_character_from_string(string_idx, char, start, end)
            else:
                old_content = self.__manager.string_list[string_idx].to_str()
                self.__manager.remove_character_from_string(string_idx, char)
            
            new_content = self.__manager.string_list[string_idx].to_str()
            
            print(f"✓ Character removed successfully!")
            print(f"  Before: '{old_content}'")
            print(f"  After:  '{new_content}'")
        except ValueError as ve:
            print(f"✗ Error: {ve}")
        except IndexError as ie:
            print(f"✗ Error: {ie}")
        except TypeError as te:
            print(f"✗ Error: {te}")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def replace_substring_ui(self):
        """UI for replacing a substring in a string."""
        try:
            print("\nCurrent strings:")
            Console.show_strings(self.__manager.string_list)
            
            string_idx = int(input("Enter string index: ").strip())
            old_substring = input("Enter substring to replace: ").strip()
            new_substring = input("Enter replacement substring: ").strip()
            
            use_count = input("Limit number of replacements? (y/n): ").strip().lower()
            if use_count == 'y':
                count = int(input("Enter number of replacements: ").strip())
                old_content = self.__manager.string_list[string_idx].to_str()
                self.__manager.replace_in_string(string_idx, old_substring, new_substring, count)
            else:
                old_content = self.__manager.string_list[string_idx].to_str()
                self.__manager.replace_in_string(string_idx, old_substring, new_substring)
            
            new_content = self.__manager.string_list[string_idx].to_str()
            
            print(f"✓ Substring replaced successfully!")
            print(f"  Before: '{old_content}'")
            print(f"  After:  '{new_content}'")
        except ValueError:
            print("✗ Error: Please enter valid numbers.")
        except IndexError as ie:
            print(f"✗ Error: {ie}")
        except TypeError as te:
            print(f"✗ Error: {te}")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def sort_by_length_ui(self):
        """UI for sorting strings by length."""
        try:
            order = input("Sort order (asc/desc): ").strip().lower()
            reverse = (order == 'desc')
            
            self.__manager.sort_by_length(reverse)
            print(f"✓ Strings sorted by length ({'descending' if reverse else 'ascending'})!")
            print("\nCurrent strings:")
            Console.show_strings(self.__manager.string_list)
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def get_total_length_ui(self):
        """UI for getting total length of all strings."""
        try:
            total = self.__manager.get_total_length()
            count = self.__manager.count_strings()
            print(f"✓ Total length of all {count} strings: {total} characters")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def clear_all_ui(self):
        """UI for clearing all strings."""
        confirm = input("Are you sure you want to clear all strings? (y/n): ").strip().lower()
        if confirm == 'y':
            try:
                self.__manager.clear_all()
                print("✓ All strings cleared successfully!")
            except Exception as e:
                print(f"✗ Error: {e}")
        else:
            print("Operation cancelled.")
    
    def undo_ui(self):
        """UI for undoing the last operation."""
        try:
            self.__manager.undo()
            print("✓ Undo successful!")
            print(f"  Current list has {self.__manager.count_strings()} strings.")
            if self.__manager.count_strings() > 0:
                print("\nCurrent strings:")
                Console.show_strings(self.__manager.string_list)
        except ValueError as ve:
            print(f"✗ Error: {ve}")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def run_demo_scenario(self):
        print("\n" + "=" * 70)
        print("RUNNING DEMO SCENARIO - All MyString Operations")
        print("=" * 70)
        
        # Create a new empty MyString
        print("\n# Create a new empty MyString")
        s = MyString('')
        print(f"s = MyString('') # the string is empty")
        print(f"Length: {len(s)}")
        
        # Create a new MyString from a given str
        print("\n# Create a new MyString from a given str")
        s1 = MyString('abcd')
        print(f"s1 = MyString('abcd') # content is now: 'abcd'")
        print(f"print(s1):")
        print(s1)
        
        # Create a new MyString with random characters
        print("\n# Create a new MyString with random characters")
        sr = MyString(initialize_with_random=True)
        print(f"sr = MyString(initialize_with_random=True)")
        print(f"Generated string: '{sr.to_str()}' (length: {len(sr)})")
        
        # Access and modify a character
        print("\n# Access and modify a character")
        if len(sr) > 2:
            print(f"print(sr[2]) # '{sr[2]}' (character at index 2)")
            old_char = sr[2]
            sr[2] = 'x'
            print(f"sr[2] = 'x' # replace '{old_char}' with 'x', content is now: '{sr.to_str()}'")
        
        # Try invalid operations
        print("\n# Try invalid operations")
        print("try:")
        print("    sr[1] = 'A' # Cannot add uppercase character")
        try:
            sr[1] = 'A'
        except TypeError as e:
            print(f"except TypeError as e:")
            print(f"    print(e)")
            print(f"    {e}")
        
        print("\ntry:")
        print("    sr[0] = '1' # Cannot add non-letter character")
        try:
            sr[0] = '1'
        except TypeError as e:
            print(f"except TypeError as e:")
            print(f"    print(e)")
            print(f"    {e}")
        
        # Insert a character
        print("\n# Insert a character")
        print(f"sr.insert(1, 'z') # insert 'z' at index 1")
        print(f"Before: '{sr.to_str()}'")
        sr.insert(1, 'z')
        print(f"After: '{sr.to_str()}'")
        
        print(f"\nsr.insert(8, 'y') # insert 'y' at the end, since 8>{len(sr)}")
        print(f"Before: '{sr.to_str()}'")
        sr.insert(8, 'y')
        print(f"After: '{sr.to_str()}'")
        
        # Remove all occurrences of a character
        print("\n# Remove all occurrences of a character")
        if 'x' in sr.to_str():
            print(f"sr.remove_character('x') # remove 'x'")
            print(f"Before: '{sr.to_str()}'")
            sr.remove_character('x')
            print(f"After: '{sr.to_str()}'")
        
        # Replace k occurrences of a substring
        print("\n# Replace k occurrences of a substring")
        s2 = MyString('abcabcabc')
        print(f"s2 = MyString('abcabcabc')")
        print(f"s2.replace('ab', 'xz', 2) # replace first 2 occurrences of 'ab' with 'xz'")
        print(f"Before: '{s2.to_str()}'")
        s2.replace('ab', 'xz', 2)
        print(f"After: '{s2.to_str()}'")
        
        # Concatenation
        print("\n# Concatenation")
        s3 = MyString('lm')
        print(f"s3 = MyString('lm')")
        print(f"sr is: '{sr.to_str()}'")
        s4 = sr + s3
        print(f"s4 = sr + s3 # content of s4: '{s4.to_str()}'")
        
        # Repetition
        print("\n# Repetition")
        print(f"sr is: '{sr.to_str()}'")
        s5 = sr * 2
        print(f"s5 = sr * 2")
        print(f"print(s5) # s5 is now: '{s5.to_str()}'")
        
        # Rotate entire string
        print("\n# Rotate entire string")
        print(f"Content of sr is now: '{sr.to_str()}'")
        sr.rotate(2)
        print(f"sr.rotate(2) # rotate right by 2 positions")
        print(f"After rotation: '{sr.to_str()}'")
        
        # Reverse a substring
        print("\n# Reverse a substring")
        print(f"Content of sr is now: '{sr.to_str()}'")
        if len(sr) >= 3:
            sr.reverse_substring(0, 2)
            print(f"sr.reverse_substring(0, 2) # reverse substring from index 0 to 2")
            print(f"After reversal: '{sr.to_str()}'")
        
        # Sliding window of size 3
        print("\n# Sliding window of size 3")
        print(f"Content is now: '{sr.to_str()}'")
        print(f"Size = 3, overlap = 2")
        if len(sr) >= 3:
            windows = sr.sliding_window(3, 2)
            print(f"windows = sr.sliding_window(3, 2)")
            print(f"Result: {windows}")
        
        print("\n" + "=" * 70)
        print("DEMO SCENARIO COMPLETED")
        print("=" * 70)
    
    def run(self):
        """Main loop for the console UI."""
        print("\n" + "=" * 60)
        print("Welcome to MyString Manager!")
        print("=" * 60)
        
        # Ask if user wants to run demo scenario
        choice = input("\nRun demo scenario? (y/n): ").strip().lower()
        if choice == 'y':
            self.run_demo_scenario()
            print("\nPress Enter to continue to interactive menu...")
            input()
        
        running = True
        while running:
            Console.print_menu()
            option = input("\n>> Choose an option: ").strip()
            
            match option:
                case "1":
                    self.add_string_ui()
                case "2":
                    self.add_default_strings_ui()
                case "3":
                    self.search_string_ui()
                case "4":
                    self.delete_string_ui()
                case "5":
                    self.remove_strings_containing_ui()
                case "6":
                    self.display_all_strings_ui()
                case "7":
                    self.filter_by_length_ui()
                case "8":
                    self.filter_by_first_character_ui()
                case "9":
                    self.concatenate_all_ui()
                case "10":
                    self.modify_character_ui()
                case "11":
                    self.rotate_string_ui()
                case "12":
                    self.insert_character_ui()
                case "13":
                    self.remove_character_ui()
                case "14":
                    self.replace_substring_ui()
                case "15":
                    self.sort_by_length_ui()
                case "16":
                    self.get_total_length_ui()
                case "17":
                    self.clear_all_ui()
                case "18":
                    self.undo_ui()
                case "x" | "X":
                    running = False
                    print("\n" + "=" * 60)
                    print("Thank you for using MyString Manager!")
                    print("=" * 60 + "\n")
                case _:
                    print("✗ Invalid option. Please try again.")
