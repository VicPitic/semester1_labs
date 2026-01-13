"""
Penguin domain entity
Represents a single penguin with its attributes
"""


class Penguin:
    def __init__(self, species: str, flipper_length_mm: float, culmen_length_mm: float,
                 culmen_depth_mm: float, body_mass_g: float, island: str, sex: str):
        """
        Initialize a Penguin object
        :param species: penguin species (Adelie, Chinstrap, Gentoo)
        :param flipper_length_mm: flipper length in mm
        :param culmen_length_mm: culmen (bill) length in mm
        :param culmen_depth_mm: culmen (bill) depth in mm
        :param body_mass_g: body mass in grams
        :param island: island where penguin was found
        :param sex: sex of the penguin (MALE, FEMALE)
        """
        self.__species = species
        self.__flipper_length_mm = flipper_length_mm
        self.__culmen_length_mm = culmen_length_mm
        self.__culmen_depth_mm = culmen_depth_mm
        self.__body_mass_g = body_mass_g
        self.__island = island
        self.__sex = sex

    # Getters
    def get_species(self) -> str:
        return self.__species

    def get_flipper_length_mm(self) -> float:
        return self.__flipper_length_mm

    def get_culmen_length_mm(self) -> float:
        return self.__culmen_length_mm

    def get_culmen_depth_mm(self) -> float:
        return self.__culmen_depth_mm

    def get_body_mass_g(self) -> float:
        return self.__body_mass_g

    def get_island(self) -> str:
        return self.__island

    def get_sex(self) -> str:
        return self.__sex

    # Setters
    def set_species(self, species: str):
        self.__species = species

    def set_flipper_length_mm(self, flipper_length_mm: float):
        self.__flipper_length_mm = flipper_length_mm

    def set_culmen_length_mm(self, culmen_length_mm: float):
        self.__culmen_length_mm = culmen_length_mm

    def set_culmen_depth_mm(self, culmen_depth_mm: float):
        self.__culmen_depth_mm = culmen_depth_mm

    def set_body_mass_g(self, body_mass_g: float):
        self.__body_mass_g = body_mass_g

    def set_island(self, island: str):
        self.__island = island

    def set_sex(self, sex: str):
        self.__sex = sex

    def get_attribute(self, attribute: str):
        """
        Get attribute value by name
        :param attribute: attribute name
        :return: attribute value
        :raises AttributeError if attribute does not exist
        """
        attribute_map = {
            'species': self.__species,
            'flipper_length_mm': self.__flipper_length_mm,
            'culmen_length_mm': self.__culmen_length_mm,
            'culmen_depth_mm': self.__culmen_depth_mm,
            'body_mass_g': self.__body_mass_g,
            'island': self.__island,
            'sex': self.__sex
        }
        if attribute not in attribute_map:
            raise AttributeError(f"Unknown attribute: {attribute}")
        return attribute_map[attribute]

    def to_dict(self) -> dict:
        """
        Convert penguin to dictionary
        :return: dictionary with all attributes
        """
        return {
            'species': self.__species,
            'flipper_length_mm': self.__flipper_length_mm,
            'culmen_length_mm': self.__culmen_length_mm,
            'culmen_depth_mm': self.__culmen_depth_mm,
            'body_mass_g': self.__body_mass_g,
            'island': self.__island,
            'sex': self.__sex
        }

    @staticmethod
    def get_numeric_attributes() -> list:
        """
        Get list of numeric attribute names
        :return: list of numeric attribute names
        """
        return ['flipper_length_mm', 'culmen_length_mm', 'culmen_depth_mm', 'body_mass_g']

    @staticmethod
    def get_string_attributes() -> list:
        """
        Get list of string attribute names
        :return: list of string attribute names
        """
        return ['species', 'island', 'sex']

    @staticmethod
    def get_all_attributes() -> list:
        """
        Get list of all attribute names
        :return: list of all attribute names
        """
        return ['species', 'flipper_length_mm', 'culmen_length_mm', 'culmen_depth_mm',
                'body_mass_g', 'island', 'sex']

    def __str__(self):
        return (f"Penguin(species={self.__species}, flipper={self.__flipper_length_mm}mm, "
                f"culmen_len={self.__culmen_length_mm}mm, culmen_depth={self.__culmen_depth_mm}mm, "
                f"mass={self.__body_mass_g}g, island={self.__island}, sex={self.__sex})")

    def __eq__(self, other):
        if not isinstance(other, Penguin):
            return False
        return (self.__species == other.__species and
                self.__flipper_length_mm == other.__flipper_length_mm and
                self.__culmen_length_mm == other.__culmen_length_mm and
                self.__culmen_depth_mm == other.__culmen_depth_mm and
                self.__body_mass_g == other.__body_mass_g and
                self.__island == other.__island and
                self.__sex == other.__sex)
