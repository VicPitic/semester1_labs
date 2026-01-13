"""
Validation classes for the Penguin Data Application
"""
from domain.penguin import Penguin
from domain.exceptions import ValidationException


class PenguinValidator:
    """Validator for Penguin objects"""

    VALID_SPECIES = ['Adelie', 'Chinstrap', 'Gentoo']
    VALID_ISLANDS = ['Torgersen', 'Biscoe', 'Dream']
    VALID_SEX = ['MALE', 'FEMALE']

    def validate_penguin(self, penguin: Penguin):
        """
        Validate a penguin object
        :param penguin: penguin to validate
        :return: -
        :raises ValidationException if penguin is not valid
        """
        errors = []

        # Validate species
        if penguin.get_species() not in self.VALID_SPECIES:
            errors.append(f"Species must be one of: {', '.join(self.VALID_SPECIES)}")

        # Validate island
        if penguin.get_island() not in self.VALID_ISLANDS:
            errors.append(f"Island must be one of: {', '.join(self.VALID_ISLANDS)}")

        # Validate sex
        if penguin.get_sex() not in self.VALID_SEX:
            errors.append(f"Sex must be one of: {', '.join(self.VALID_SEX)}")

        # Validate numeric attributes (must be positive)
        if penguin.get_flipper_length_mm() <= 0:
            errors.append("Flipper length must be positive")

        if penguin.get_culmen_length_mm() <= 0:
            errors.append("Culmen length must be positive")

        if penguin.get_culmen_depth_mm() <= 0:
            errors.append("Culmen depth must be positive")

        if penguin.get_body_mass_g() <= 0:
            errors.append("Body mass must be positive")

        if errors:
            raise ValidationException("; ".join(errors))


class CommandValidator:
    """Validator for CLI commands"""

    VALID_COMMANDS = [
        'print', 'load', 'filter', 'describe', 'unique',
        'sort', 'augment', 'scatter', 'hist', 'boxplot',
        'help', 'quit', 'classify', 'random_fact', 'draw_penguin'
    ]

    VALID_SORT_ORDERS = ['asc', 'desc']
    VALID_AUGMENT_MODES = ['duplicate', 'create']
    VALID_GROUPBY = ['island', 'species']

    def validate_command(self, command: str) -> bool:
        """
        Validate if command is recognized
        :param command: command to validate
        :return: True if valid
        """
        return command.lower() in self.VALID_COMMANDS

    def validate_sort_order(self, order: str) -> bool:
        """
        Validate sort order
        :param order: order string
        :return: True if valid
        """
        return order.lower() in self.VALID_SORT_ORDERS

    def validate_augment_mode(self, mode: str) -> bool:
        """
        Validate augment mode
        :param mode: mode string
        :return: True if valid
        """
        return mode.lower() in self.VALID_AUGMENT_MODES

    def validate_groupby(self, groupby: str) -> bool:
        """
        Validate groupby parameter for boxplot
        :param groupby: groupby string
        :return: True if valid
        """
        return groupby.lower() in self.VALID_GROUPBY
