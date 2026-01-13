import random
import string


class MyString:
    def __init__(self, s='', initialize_with_random=False):
        if initialize_with_random:
            n = random.randint(1, 10)
            self.__chars = [random.choice(string.ascii_lowercase) for _ in range(n)]
        else:
            # Validate the string
            for char in s:
                if not char.islower() or not char.isalpha():
                    raise TypeError(f"Only lowercase letters allowed, got '{char}'")
            self.__chars = list(s)
    
    def __len__(self):
        return len(self.__chars)
    
    def __getitem__(self, index):
        return self.__chars[index]
    
    def __setitem__(self, index, char):
        if not isinstance(char, str) or len(char) != 1:
            raise TypeError("Must be a single character")
        if not char.islower():
            raise TypeError(f"Only lowercase characters are allowed, got '{char}'")
        if not char.isalpha():
            raise TypeError(f"Only alphabetic characters are allowed, got '{char}'")
        self.__chars[index] = char
    
    def __str__(self):
        result = ''.join(self.__chars)
        if self.__chars:
            for i, char in enumerate(self.__chars):
                result += f"\nCharacter at position {i}: {char}"
        return result
    
    def __repr__(self):
        return f"MyString('{''.join(self.__chars)}')"
    
    def __add__(self, other):
        if not isinstance(other, MyString):
            raise TypeError(f"Can only concatenate MyString with MyString")
        result = MyString('')
        result.__chars = self.__chars + other.__chars
        return result
    
    def __mul__(self, n):
        if not isinstance(n, int):
            raise TypeError(f"Can't multiply MyString by non-int")
        if n < 0:
            raise ValueError(f"Can't multiply MyString by negative number")
        result = MyString('')
        result.__chars = self.__chars * n
        return result
    
    def __eq__(self, other):
        """Two MyString objects are equal if the sum of ASCII codes of their characters is the same."""
        if not isinstance(other, MyString):
            return False
        
        # Calculate sum of ASCII codes for self
        sum_self = sum(ord(char) for char in self.__chars)
        
        # Calculate sum of ASCII codes for other
        sum_other = sum(ord(char) for char in other.__chars)

        return sum_self == sum_other
    
    def to_str(self):
        return ''.join(self.__chars)
    
    def insert(self, position, char):
        if not isinstance(char, str) or len(char) != 1:
            raise TypeError("Must be a single character")
        if not char.islower() or not char.isalpha():
            raise TypeError(f"Only lowercase letters allowed")
        
        if position >= len(self.__chars):
            self.__chars.append(char)
        else:
            self.__chars.insert(position, char)
    
    def remove_character(self, char, start=0, end=None):
        if not isinstance(char, str) or len(char) != 1:
            raise TypeError("Must be a single character")
        if not char.islower() or not char.isalpha():
            raise TypeError(f"Only lowercase letters allowed")
        
        if end is None:
            end = len(self.__chars) - 1
        
        # Check if character exists in range
        found = False
        for i in range(start, min(end + 1, len(self.__chars))):
            if self.__chars[i] == char:
                found = True
                break
        
        if not found:
            raise ValueError(f"Character '{char}' not found in string")
        
        # Remove all occurrences in range
        i = min(end, len(self.__chars) - 1)
        while i >= start:
            if self.__chars[i] == char:
                self.__chars.pop(i)
            i -= 1
    
    def replace(self, old, new, count=None):
        # Validate strings
        for char in old:
            if not char.islower() or not char.isalpha():
                raise TypeError(f"Only lowercase letters allowed")
        for char in new:
            if not char.islower() or not char.isalpha():
                raise TypeError(f"Only lowercase letters allowed")
        
        if not old:
            return
        
        current_str = ''.join(self.__chars)
        
        if count is None:
            result_str = current_str.replace(old, new)
        else:
            result_str = current_str.replace(old, new, count)
        
        self.__chars = list(result_str)
    
    def find(self, substring):
        for char in substring:
            if not char.islower() or not char.isalpha():
                raise TypeError(f"Only lowercase letters allowed")
        
        current_str = ''.join(self.__chars)
        return current_str.find(substring)
    
    def rotate(self, n):
        if len(self.__chars) == 0:
            return
        
        n = n % len(self.__chars)
        
        if n == 0:
            return
        
        self.__chars = self.__chars[-n:] + self.__chars[:-n]
    
    def reverse_substring(self, start, end):
        if start < 0 or end >= len(self.__chars) or start > end:
            return
        
        while start < end:
            self.__chars[start], self.__chars[end] = self.__chars[end], self.__chars[start]
            start += 1
            end -= 1
    
    def sliding_window(self, size, overlap):
        if size <= 0 or overlap < 0 or overlap >= size:
            return []
        
        windows = []
        step = size - overlap
        current_str = ''.join(self.__chars)
        
        i = 0
        while i + size <= len(current_str):
            windows.append(current_str[i:i + size])
            i += step
        
        return windows
