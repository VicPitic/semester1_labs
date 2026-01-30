"""
Statistics Service
Handles visualization and statistical plotting for penguin data
"""
import matplotlib.pyplot as plt

from domain.penguin import Penguin
from domain.exceptions import (
    NoDataLoadedException, InvalidAttributeException, NonNumericAttributeException
)
from repository.penguin_repo import PenguinRepo


class StatsService:
    def __init__(self, penguin_repo: PenguinRepo):
        self.__penguin_repo = penguin_repo

    def _check_data_loaded(self):
        """Check if data is loaded"""
        if self.__penguin_repo.get_penguin_count() == 0:
            raise NoDataLoadedException()

    def _validate_attribute(self, attribute: str):
        """Validate attribute exists"""
        if attribute not in Penguin.get_all_attributes():
            raise InvalidAttributeException(attribute, Penguin.get_all_attributes())

    def _validate_numeric_attribute(self, attribute: str):
        """Validate attribute is numeric"""
        self._validate_attribute(attribute)
        if attribute not in Penguin.get_numeric_attributes():
            raise NonNumericAttributeException(attribute, "plotting")

    def scatter_plot(self, attr1: str, attr2: str):
        """
        Generate a scatter plot for two numeric attributes
        :param attr1: first attribute (x-axis)
        :param attr2: second attribute (y-axis)
        :raises NonNumericAttributeException if attributes are not numeric
        """
        self._check_data_loaded()
        self._validate_numeric_attribute(attr1)
        self._validate_numeric_attribute(attr2)

        penguins = self.__penguin_repo.get_all_penguins()
        x_values = [p.get_attribute(attr1) for p in penguins]
        y_values = [p.get_attribute(attr2) for p in penguins]

        # Color by species
        species_list = [p.get_species() for p in penguins]
        unique_species = list(set(species_list))
        colors = {'Adelie': 'red', 'Chinstrap': 'green', 'Gentoo': 'blue'}

        plt.figure(figsize=(10, 6))
        for species in unique_species:
            x_sp = [x_values[i] for i in range(len(penguins)) if species_list[i] == species]
            y_sp = [y_values[i] for i in range(len(penguins)) if species_list[i] == species]
            plt.scatter(x_sp, y_sp, c=colors.get(species, 'gray'), label=species, alpha=0.7)

        plt.xlabel(attr1)
        plt.ylabel(attr2)
        plt.title(f'Scatter Plot: {attr1} vs {attr2}')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    def histogram(self, attribute: str, bins: int):
        """
        Generate a histogram for a numeric attribute
        :param attribute: numeric attribute
        :param bins: number of bins
        :raises NonNumericAttributeException if attribute is not numeric
        """
        self._check_data_loaded()
        self._validate_numeric_attribute(attribute)

        penguins = self.__penguin_repo.get_all_penguins()
        values = [p.get_attribute(attribute) for p in penguins]

        plt.figure(figsize=(10, 6))
        plt.hist(values, bins=bins, edgecolor='black', alpha=0.7, color='steelblue')
        plt.xlabel(attribute)
        plt.ylabel('Frequency')
        plt.title(f'Histogram of {attribute}')
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.show()

    def boxplot(self, groupby: str, attribute: str):
        """
        Generate a boxplot grouped by island or species
        :param groupby: 'island' or 'species'
        :param attribute: numeric attribute to plot
        :raises NonNumericAttributeException if attribute is not numeric
        """
        self._check_data_loaded()
        self._validate_numeric_attribute(attribute)

        if groupby not in ['island', 'species']:
            raise InvalidAttributeException(groupby, ['island', 'species'])

        penguins = self.__penguin_repo.get_all_penguins()
        
        # Group data
        groups = {}
        for penguin in penguins:
            group_key = penguin.get_attribute(groupby)
            if group_key not in groups:
                groups[group_key] = []
            groups[group_key].append(penguin.get_attribute(attribute))

        # Sort groups for consistent display
        sorted_groups = sorted(groups.keys())
        data = [groups[g] for g in sorted_groups]

        plt.figure(figsize=(10, 6))
        bp = plt.boxplot(data, labels=sorted_groups, patch_artist=True)
        
        # Color boxes
        colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightcoral']
        for i, patch in enumerate(bp['boxes']):
            patch.set_facecolor(colors[i % len(colors)])

        plt.xlabel(groupby.capitalize())
        plt.ylabel(attribute)
        plt.title(f'Boxplot of {attribute} by {groupby.capitalize()}')
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.show()
