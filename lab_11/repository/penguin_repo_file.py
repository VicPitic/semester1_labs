"""
File-based Penguin Repository
Handles CSV file operations for penguin data
"""
import os
import csv
from domain.penguin import Penguin
from domain.exceptions import FileNotFoundException


class PenguinRepoFile:
    def __init__(self, data_directory: str = "data"):
        """
        Initialize file repository
        :param data_directory: directory where CSV files are stored
        """
        self.__data_directory = data_directory
        self._ensure_directory_exists()

    def _ensure_directory_exists(self):
        """Create data directory if it doesn't exist"""
        if not os.path.exists(self.__data_directory):
            os.makedirs(self.__data_directory)

    def get_data_directory(self) -> str:
        """Get the data directory path"""
        return self.__data_directory

    def get_available_files(self) -> list:
        """
        Get list of all CSV files in the data directory
        :return: list of CSV filenames
        """
        try:
            files = os.listdir(self.__data_directory)
            return [f for f in files if f.endswith('.csv')]
        except FileNotFoundError:
            return []

    def load_from_file(self, filename: str) -> list:
        """
        Load penguins from a CSV file
        :param filename: name of the file to load
        :return: list of Penguin objects
        :raises FileNotFoundException if file doesn't exist
        """
        filepath = os.path.join(self.__data_directory, filename)
        if not os.path.exists(filepath):
            raise FileNotFoundException(filename)

        penguins = []
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            
            for values in reader:
                if len(values) < 7:
                    continue

                try:
                    penguin = self._create_penguin_from_row(header, values)
                    if penguin:
                        penguins.append(penguin)
                except (ValueError, IndexError):
                    # Skip invalid rows
                    continue

        return penguins

    def _create_penguin_from_row(self, header: list, values: list) -> Penguin:
        """
        Create a Penguin object from CSV row data
        Handles both raw penguins.csv format and preprocessed penguins_data.csv format
        :param header: list of column names
        :param values: list of values
        :return: Penguin object or None if invalid
        """
        # Create a mapping from header to values
        data = {header[i].strip(): values[i].strip() for i in range(min(len(header), len(values)))}

        # Map possible column names (support both raw and preprocessed formats)
        # Species: handle full name like "Adelie Penguin (Pygoscelis adeliae)" -> "Adelie"
        species_raw = data.get('species', '') or data.get('Species', '')
        if 'Adelie' in species_raw:
            species = 'Adelie'
        elif 'Chinstrap' in species_raw:
            species = 'Chinstrap'
        elif 'Gentoo' in species_raw:
            species = 'Gentoo'
        else:
            species = species_raw

        # Numeric fields: support both naming conventions
        flipper = self._parse_float(
            data.get('flipper_length_mm', '') or data.get('Flipper Length (mm)', '')
        )
        culmen_len = self._parse_float(
            data.get('culmen_length_mm', '') or data.get('Culmen Length (mm)', '')
        )
        culmen_depth = self._parse_float(
            data.get('culmen_depth_mm', '') or data.get('Culmen Depth (mm)', '')
        )
        body_mass = self._parse_float(
            data.get('body_mass_g', '') or data.get('Body Mass (g)', '')
        )

        # String fields
        island = data.get('island', '') or data.get('Island', '')
        sex = (data.get('sex', '') or data.get('Sex', '')).upper()

        # Validate all required fields are present
        if not all([species, island, sex]) or None in [flipper, culmen_len, culmen_depth, body_mass]:
            return None

        return Penguin(species, flipper, culmen_len, culmen_depth, body_mass, island, sex)

    @staticmethod
    def _parse_float(value: str):
        """
        Parse string to float, return None if invalid
        :param value: string value
        :return: float or None
        """
        try:
            return float(value)
        except (ValueError, TypeError):
            return None

    def save_to_file(self, filename: str, penguins: list):
        """
        Save penguins to a CSV file
        :param filename: name of the file to save to
        :param penguins: list of Penguin objects
        :return: -
        """
        filepath = os.path.join(self.__data_directory, filename)
        
        with open(filepath, 'w', encoding='utf-8') as file:
            # Write header
            header = "species,flipper_length_mm,culmen_length_mm,culmen_depth_mm,body_mass_g,island,sex\n"
            file.write(header)

            # Write data rows
            for penguin in penguins:
                row = (f"{penguin.get_species()},{penguin.get_flipper_length_mm()},"
                       f"{penguin.get_culmen_length_mm()},{penguin.get_culmen_depth_mm()},"
                       f"{penguin.get_body_mass_g()},{penguin.get_island()},{penguin.get_sex()}\n")
                file.write(row)

    def preprocess_raw_data(self, input_filename: str, output_filename: str):
        """
        Preprocess raw penguins.csv to create cleaned penguins_data.csv
        Only keeps rows with all 7 required fields having valid data
        :param input_filename: raw input file name
        :param output_filename: cleaned output file name
        :return: number of valid rows saved
        """
        input_path = os.path.join(self.__data_directory, input_filename)
        if not os.path.exists(input_path):
            raise FileNotFoundException(input_filename)

        valid_penguins = []
        required_columns = ['species', 'flipper_length_mm', 'culmen_length_mm', 
                           'culmen_depth_mm', 'body_mass_g', 'island', 'sex']

        with open(input_path, 'r', encoding='utf-8') as file:
            header = file.readline().strip().split(',')
            header = [h.strip() for h in header]

            # Find column indices
            col_indices = {}
            for col in required_columns:
                if col in header:
                    col_indices[col] = header.index(col)
                else:
                    # Try case-insensitive match
                    for i, h in enumerate(header):
                        if h.lower() == col.lower():
                            col_indices[col] = i
                            break

            for line in file:
                line = line.strip()
                if not line:
                    continue

                values = line.split(',')
                
                try:
                    # Extract required values
                    row_data = {}
                    valid_row = True
                    
                    for col in required_columns:
                        if col not in col_indices or col_indices[col] >= len(values):
                            valid_row = False
                            break
                        
                        val = values[col_indices[col]].strip()
                        if not val or val.upper() == 'NA' or val == '.':
                            valid_row = False
                            break
                        
                        row_data[col] = val

                    if not valid_row:
                        continue

                    # Validate numeric fields
                    flipper = self._parse_float(row_data['flipper_length_mm'])
                    culmen_len = self._parse_float(row_data['culmen_length_mm'])
                    culmen_depth = self._parse_float(row_data['culmen_depth_mm'])
                    body_mass = self._parse_float(row_data['body_mass_g'])

                    if None in [flipper, culmen_len, culmen_depth, body_mass]:
                        continue

                    penguin = Penguin(
                        row_data['species'],
                        flipper,
                        culmen_len,
                        culmen_depth,
                        body_mass,
                        row_data['island'],
                        row_data['sex'].upper()
                    )
                    valid_penguins.append(penguin)

                except (ValueError, IndexError, KeyError):
                    continue

        # Save valid data
        self.save_to_file(output_filename, valid_penguins)
        return len(valid_penguins)
