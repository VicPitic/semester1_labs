"""
Penguin Service
Business logic for penguin data operations including filter, describe, unique, sort, augment
"""
import random
import time
from datetime import datetime

from domain.penguin import Penguin
from domain.exceptions import (
    NoDataLoadedException, InvalidAttributeException, NonNumericAttributeException,
    InvalidSortOrderException, InvalidPercentageException, InvalidAugmentModeException,
    EmptyDatasetException, InvalidFilterValueException
)
from repository.penguin_repo import PenguinRepo
from repository.penguin_repo_file import PenguinRepoFile


class PenguinService:
    def __init__(self, penguin_repo: PenguinRepo, penguin_repo_file: PenguinRepoFile):
        self.__penguin_repo = penguin_repo
        self.__penguin_repo_file = penguin_repo_file
        self.__current_file = None
        self.__sort_log_file = "sort_performance.log"

    def get_available_files(self) -> list:
        """
        Get list of available CSV files
        :return: list of filenames
        """
        return self.__penguin_repo_file.get_available_files()

    def load_data(self, filename: str) -> int:
        """
        Load data from a CSV file
        :param filename: filename to load
        :return: number of penguins loaded
        """
        penguins = self.__penguin_repo_file.load_from_file(filename)
        self.__penguin_repo.clear()
        self.__penguin_repo.add_all(penguins)
        self.__current_file = filename
        return len(penguins)

    def get_loaded_penguins(self) -> list:
        """
        Get all loaded penguins
        :return: list of penguins
        """
        return self.__penguin_repo.get_all_penguins()

    def get_penguin_count(self) -> int:
        """
        Get count of loaded penguins
        :return: count
        """
        return self.__penguin_repo.get_penguin_count()

    def _check_data_loaded(self):
        """Check if data is loaded, raise exception if not"""
        if self.__penguin_repo.get_penguin_count() == 0:
            raise NoDataLoadedException()

    def _validate_attribute(self, attribute: str):
        """Validate that attribute exists"""
        if attribute not in Penguin.get_all_attributes():
            raise InvalidAttributeException(attribute, Penguin.get_all_attributes())

    def _is_numeric_attribute(self, attribute: str) -> bool:
        """Check if attribute is numeric"""
        return attribute in Penguin.get_numeric_attributes()

    # ==================== FILTER ====================
    def filter_data(self, attribute: str, value: str) -> list:
        """
        Filter penguins by attribute and value
        For numeric attributes: returns penguins where attribute > value
        For string attributes: returns penguins where attribute == value
        
        Time Complexity: O(n) where n is the number of penguins
        Space Complexity: O(k) where k is the number of matching penguins
        
        :param attribute: attribute to filter by
        :param value: value to compare against
        :return: list of matching penguins
        :raises NoDataLoadedException if no data loaded
        :raises InvalidAttributeException if attribute doesn't exist
        :raises InvalidFilterValueException if value type doesn't match
        """
        self._check_data_loaded()
        self._validate_attribute(attribute)

        is_numeric = self._is_numeric_attribute(attribute)

        if is_numeric:
            try:
                numeric_value = float(value)
            except ValueError:
                raise InvalidFilterValueException(value, "numeric")
            return self.__penguin_repo.get_penguins_by_filter(attribute, numeric_value, True)
        else:
            return self.__penguin_repo.get_penguins_by_filter(attribute, value, False)

    def save_filtered_data(self, penguins: list, filename: str):
        """
        Save filtered penguins to a file
        :param penguins: list of penguins to save
        :param filename: filename to save to
        """
        self.__penguin_repo_file.save_to_file(filename, penguins)

    # ==================== DESCRIBE ====================
    def describe_attribute(self, attribute: str) -> dict:
        """
        Calculate min, max, and mean for a numeric attribute
        
        Time Complexity: O(n) where n is the number of penguins
        Space Complexity: O(1) - only stores min, max, sum, count
        
        :param attribute: numeric attribute to describe
        :return: dictionary with min, max, mean values
        :raises NoDataLoadedException if no data loaded
        :raises InvalidAttributeException if attribute doesn't exist
        :raises NonNumericAttributeException if attribute is not numeric
        """
        self._check_data_loaded()
        self._validate_attribute(attribute)

        if not self._is_numeric_attribute(attribute):
            raise NonNumericAttributeException(attribute, "describe")

        values = self.__penguin_repo.get_attribute_values(attribute)
        
        if not values:
            raise EmptyDatasetException()

        min_val = values[0]
        max_val = values[0]
        total = 0

        for val in values:
            if val < min_val:
                min_val = val
            if val > max_val:
                max_val = val
            total += val

        mean_val = total / len(values)

        return {
            'min': min_val,
            'max': max_val,
            'mean': round(mean_val, 2)
        }

    # ==================== UNIQUE ====================
    def unique_values(self, attribute: str) -> dict:
        """
        Get unique values and their counts for an attribute
        
        Time Complexity: O(n) where n is the number of penguins
        Space Complexity: O(k) where k is the number of unique values
        
        :param attribute: attribute to get unique values for
        :return: dictionary mapping values to counts
        :raises NoDataLoadedException if no data loaded
        :raises InvalidAttributeException if attribute doesn't exist
        """
        self._check_data_loaded()
        self._validate_attribute(attribute)

        values = self.__penguin_repo.get_attribute_values(attribute)
        
        counts = {}
        for val in values:
            if val in counts:
                counts[val] += 1
            else:
                counts[val] = 1

        return counts

    # ==================== SORT ====================
    def sort_data(self, attribute: str, order: str) -> list:
        """
        Sort penguins by attribute using custom sorting algorithm
        Uses Insertion Sort (based on name requirements)
        
        Time Complexity: O(n^2) for Insertion Sort
        Space Complexity: O(1) in-place sorting
        
        :param attribute: attribute to sort by
        :param order: 'asc' or 'desc'
        :return: sorted list of penguins
        :raises NoDataLoadedException if no data loaded
        :raises InvalidAttributeException if attribute doesn't exist
        :raises InvalidSortOrderException if order is invalid
        """
        self._check_data_loaded()
        self._validate_attribute(attribute)

        order = order.lower()
        if order not in ['asc', 'desc']:
            raise InvalidSortOrderException(order)

        penguins = self.__penguin_repo.get_all_penguins().copy()
        n = len(penguins)

        # Measure execution time
        start_time = time.time()

        # Selection Sort
        for i in range(n - 1):
            # Find the min/max element in remaining unsorted portion
            extreme_idx = i
            extreme_value = penguins[i].get_attribute(attribute)

            for j in range(i + 1, n):
                current_value = penguins[j].get_attribute(attribute)
                if order == 'asc':
                    if current_value < extreme_value:
                        extreme_idx = j
                        extreme_value = current_value
                else:  # desc
                    if current_value > extreme_value:
                        extreme_idx = j
                        extreme_value = current_value

            # Swap if needed
            if extreme_idx != i:
                penguins[i], penguins[extreme_idx] = penguins[extreme_idx], penguins[i]

        execution_time = time.time() - start_time

        # Log performance
        self._log_sort_performance(n, "SelectionSort", execution_time)

        # Update repository with sorted data
        self.__penguin_repo.set_penguins(penguins)

        return penguins

    def _log_sort_performance(self, num_rows: int, algorithm: str, execution_time: float):
        """
        Log sort performance to file
        Format: date_of_run, time_of_run, number_of_rows, sorting_algorithm, execution_time_in_seconds
        """
        now = datetime.now()
        log_entry = f"{now.strftime('%Y-%m-%d')}, {now.strftime('%H:%M:%S')}, {num_rows}, {algorithm}, {execution_time:.6f}\n"
        
        with open(self.__sort_log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)

    # ==================== AUGMENT ====================
    def augment_data(self, percent: float, mode: str) -> tuple:
        """
        Increase dataset size by percentage
        
        :param percent: percentage to increase by
        :param mode: 'duplicate' or 'create'
        :return: tuple (new list of penguins, suggested filename)
        :raises NoDataLoadedException if no data loaded
        :raises InvalidPercentageException if percent is invalid
        :raises InvalidAugmentModeException if mode is invalid
        """
        self._check_data_loaded()

        try:
            percent = float(percent)
            if percent <= 0:
                raise ValueError()
        except ValueError:
            raise InvalidPercentageException(percent)

        mode = mode.lower()
        if mode not in ['duplicate', 'create']:
            raise InvalidAugmentModeException(mode)

        penguins = self.__penguin_repo.get_all_penguins()
        original_count = len(penguins)
        new_count = int(original_count * percent / 100)

        new_penguins = penguins.copy()

        if mode == 'duplicate':
            # Randomly duplicate existing entries
            for _ in range(new_count):
                random_penguin = random.choice(penguins)
                new_penguins.append(random_penguin)
        else:  # create
            # Generate new entries with random valid values
            new_penguins.extend(self._generate_random_penguins(penguins, new_count))

        filename = f"augmented_{mode}_{int(percent)}pct_{len(new_penguins)}.csv"
        return new_penguins, filename

    def _generate_random_penguins(self, existing: list, count: int) -> list:
        """
        Generate new penguins using values from existing data
        Strings: randomly chosen from existing
        Numerics: random value between min and max
        """
        if not existing:
            return []

        # Get ranges for numeric attributes
        numeric_ranges = {}
        for attr in Penguin.get_numeric_attributes():
            values = [p.get_attribute(attr) for p in existing]
            numeric_ranges[attr] = (min(values), max(values))

        # Get unique string values
        string_values = {}
        for attr in Penguin.get_string_attributes():
            string_values[attr] = list(set(p.get_attribute(attr) for p in existing))

        new_penguins = []
        for _ in range(count):
            species = random.choice(string_values['species'])
            island = random.choice(string_values['island'])
            sex = random.choice(string_values['sex'])

            flipper = random.uniform(*numeric_ranges['flipper_length_mm'])
            culmen_len = random.uniform(*numeric_ranges['culmen_length_mm'])
            culmen_depth = random.uniform(*numeric_ranges['culmen_depth_mm'])
            body_mass = random.uniform(*numeric_ranges['body_mass_g'])

            new_penguins.append(Penguin(
                species, round(flipper, 1), round(culmen_len, 1),
                round(culmen_depth, 1), round(body_mass, 1), island, sex
            ))

        return new_penguins

    def save_augmented_data(self, penguins: list, filename: str):
        """Save augmented data to file"""
        self.__penguin_repo_file.save_to_file(filename, penguins)

    # ==================== SAVE RANDOM ====================
    def save_random(self, k: int, filename: str) -> list:
        """
        Choose k penguins randomly from the currently loaded dataset and save to file
        
        Time Complexity: O(k) for random selection using random.sample
        Space Complexity: O(k) for storing the selected penguins
        
        :param k: number of penguins to select
        :param filename: filename to save to
        :return: list of selected penguins
        :raises NoDataLoadedException if no data loaded
        :raises ValueError if k is invalid
        """
        self._check_data_loaded()
        
        penguins = self.__penguin_repo.get_all_penguins()
        
        if k <= 0:
            raise ValueError("k must be a positive integer")
        if k > len(penguins):
            raise ValueError(f"k ({k}) cannot be greater than the number of loaded penguins ({len(penguins)})")
        
        # Randomly select k penguins
        selected = random.sample(penguins, k)
        
        # Save to file
        if not filename.endswith('.csv'):
            filename += '.csv'
        self.__penguin_repo_file.save_to_file(filename, selected)
        
        return selected

    # ==================== GENERATE RESEARCH GROUPS ====================
    def generate_research_groups(self, k: int) -> list:
        """
        Generate all possible research groups of size k with at least one penguin from each species
        Requires at most 10 penguins in loaded dataset
        
        Time Complexity: O(C(n,k)) where C(n,k) is n choose k combinations
        Space Complexity: O(C(n,k) * k) for storing all valid groups
        
        :param k: size of research groups (must be >= 3)
        :return: list of valid research groups (each group is a list of penguins)
        :raises NoDataLoadedException if no data loaded
        :raises ValueError if constraints not met
        """
        self._check_data_loaded()
        
        penguins = self.__penguin_repo.get_all_penguins()
        
        if len(penguins) > 10:
            raise ValueError(f"Dataset must contain at most 10 penguins (current: {len(penguins)})")
        
        if k < 3:
            raise ValueError("Group size k must be at least 3")
        
        if k > len(penguins):
            raise ValueError(f"k ({k}) cannot be greater than the number of penguins ({len(penguins)})")
        
        # Get unique species in the dataset
        species_in_data = set(p.get_species() for p in penguins)
        
        if len(species_in_data) < 1:
            raise ValueError("No species found in dataset")
        
        # Generate all combinations of size k
        valid_groups = []
        
        def generate_combinations(start: int, current_group: list):
            """Recursively generate combinations"""
            if len(current_group) == k:
                # Check if group has at least one penguin from each species present in data
                group_species = set(p.get_species() for p in current_group)
                if len(group_species) >= min(3, len(species_in_data)) and len(group_species) == len(species_in_data):
                    valid_groups.append(current_group.copy())
                return
            
            for i in range(start, len(penguins)):
                current_group.append(penguins[i])
                generate_combinations(i + 1, current_group)
                current_group.pop()
        
        generate_combinations(0, [])
        
        return valid_groups

    # ==================== SPLIT INTO GROUPS ====================
    def split_into_groups(self, body_mass_threshold: float) -> list:
        """
        Generate all possible ways to split penguins into two groups such that:
        - Each group has at least 2 penguins
        - Total body mass of each group does not exceed threshold
        Requires at most 10 penguins in loaded dataset
        
        Time Complexity: O(2^n) for generating all possible splits
        Space Complexity: O(2^n) for storing all valid splits
        
        :param body_mass_threshold: maximum total body mass for each group
        :return: list of valid splits (each split is a tuple of two groups)
        :raises NoDataLoadedException if no data loaded
        :raises ValueError if constraints not met
        """
        self._check_data_loaded()
        
        penguins = self.__penguin_repo.get_all_penguins()
        n = len(penguins)
        
        if n > 10:
            raise ValueError(f"Dataset must contain at most 10 penguins (current: {n})")
        
        if n < 4:
            raise ValueError(f"Need at least 4 penguins to split into two groups of 2 (current: {n})")
        
        valid_splits = []
        
        def get_group_mass(group: list) -> float:
            """Calculate total body mass of a group"""
            return sum(p.get_body_mass_g() for p in group)
        
        def generate_splits(index: int, group1: list, group2: list):
            """Recursively generate all possible splits"""
            if index == n:
                # Check constraints
                if len(group1) >= 2 and len(group2) >= 2:
                    mass1 = get_group_mass(group1)
                    mass2 = get_group_mass(group2)
                    if mass1 <= body_mass_threshold and mass2 <= body_mass_threshold:
                        # Store as tuple of lists
                        valid_splits.append((group1.copy(), group2.copy()))
                return
            
            # Try adding current penguin to group1
            group1.append(penguins[index])
            generate_splits(index + 1, group1, group2)
            group1.pop()
            
            # Try adding current penguin to group2
            group2.append(penguins[index])
            generate_splits(index + 1, group1, group2)
            group2.pop()
        
        generate_splits(0, [], [])
        
        # Remove duplicate splits (group1, group2) and (group2, group1) are the same
        unique_splits = []
        seen = set()
        for g1, g2 in valid_splits:
            # Create a hashable representation
            key1 = tuple(sorted(id(p) for p in g1))
            key2 = tuple(sorted(id(p) for p in g2))
            normalized_key = tuple(sorted([key1, key2]))
            if normalized_key not in seen:
                seen.add(normalized_key)
                unique_splits.append((g1, g2))
        
        return unique_splits

    # ==================== PREPROCESS ====================
    def preprocess_data(self, input_file: str, output_file: str) -> int:
        """
        Preprocess raw data file
        :param input_file: raw input filename
        :param output_file: cleaned output filename
        :return: number of valid rows
        """
        return self.__penguin_repo_file.preprocess_raw_data(input_file, output_file)
