"""
In-memory Penguin Repository
Handles CRUD operations for penguins in memory
"""
from domain.penguin import Penguin


class PenguinRepo:
    def __init__(self):
        self.__penguins = []

    def add_penguin(self, penguin: Penguin):
        """
        Add a penguin to the repository
        :param penguin: penguin to add
        :return: -
        """
        self.__penguins.append(penguin)

    def add_all(self, penguins: list):
        """
        Add multiple penguins to the repository
        :param penguins: list of penguins
        :return: -
        """
        self.__penguins.extend(penguins)

    def get_all_penguins(self) -> list:
        """
        Get all penguins
        :return: list of all penguins
        """
        return self.__penguins

    def get_penguin_count(self) -> int:
        """
        Get the number of penguins
        :return: count of penguins
        """
        return len(self.__penguins)

    def clear(self):
        """
        Remove all penguins from repository
        :return: -
        """
        self.__penguins = []

    def set_penguins(self, penguins: list):
        """
        Replace all penguins with new list
        :param penguins: new list of penguins
        :return: -
        """
        self.__penguins = penguins

    def get_penguins_by_filter(self, attribute: str, value, is_numeric: bool) -> list:
        """
        Get penguins filtered by attribute value
        For numeric: returns penguins where attribute > value
        For string: returns penguins where attribute == value
        
        Time Complexity: O(n) where n is the number of penguins
        Space Complexity: O(k) where k is the number of matching penguins
        
        :param attribute: attribute name to filter by
        :param value: value to compare against
        :param is_numeric: True if numeric comparison (>), False if string comparison (==)
        :return: list of matching penguins
        """
        result = []
        for penguin in self.__penguins:
            attr_value = penguin.get_attribute(attribute)
            if is_numeric:
                if attr_value > value:
                    result.append(penguin)
            else:
                if attr_value == value:
                    result.append(penguin)
        return result

    def get_attribute_values(self, attribute: str) -> list:
        """
        Get all values for a specific attribute
        
        Time Complexity: O(n) where n is the number of penguins
        Space Complexity: O(n) for the result list
        
        :param attribute: attribute name
        :return: list of attribute values
        """
        return [penguin.get_attribute(attribute) for penguin in self.__penguins]
