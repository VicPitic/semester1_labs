"""
Console UI
Command-line interface for the Penguin Data Application
"""
import random

from domain.penguin import Penguin
from domain.exceptions import (
    PenguinAppException, InvalidCommandException, FileNotFoundException
)
from service.penguin_service import PenguinService
from service.stats_service import StatsService
from service.classifier_service import ClassifierService


class Console:
    def __init__(self, penguin_service: PenguinService, stats_service: StatsService,
                 classifier_service: ClassifierService):
        self.__penguin_service = penguin_service
        self.__stats_service = stats_service
        self.__classifier_service = classifier_service
        self.__penguin_facts = [
            "Emperor penguins can dive to depths of over 500 meters!",
            "Penguins have excellent hearing and can identify their mates by their calls.",
            "The smallest penguin species is the Little Blue Penguin, standing just 33cm tall.",
            "Penguins are found in every continent of the Southern Hemisphere.",
            "A group of penguins in water is called a 'raft', on land they're a 'waddle'.",
            "Penguins can drink salt water because they have special glands that filter out salt.",
            "Emperor penguins can survive temperatures as low as -60°C.",
            "Penguins are carnivores and eat fish, squid, and krill.",
            "Some penguin species can swim up to 22 miles per hour.",
            "Penguins spend about 75% of their lives in water.",
            "Male Emperor penguins incubate eggs for about 65 days without eating.",
            "Penguins have been around for about 60 million years.",
            "The yellow-eyed penguin is one of the rarest penguin species.",
            "Penguins can recognize individual faces, even in a crowd.",
            "Chinstrap penguins get their name from the thin black band under their chin."
        ]

    @staticmethod
    def print_menu():
        """Print full help menu with all available commands"""
        print("\n" + "=" * 60)
        print("PENGUIN DATA ANALYZER - Available Commands")
        print("=" * 60)
        print("\nData Management:")
        print("  print available_data    - List all CSV files in data directory")
        print("  load <filename>         - Load data from a CSV file")
        print("  save_random <k> <file>  - Save k random penguins to file")
        print("\nData Analysis:")
        print("  filter <attr> <value>   - Filter data by attribute")
        print("                            Numeric: keeps rows where attr > value")
        print("                            String: keeps rows where attr == value")
        print("  describe <attr>         - Show min, max, mean for numeric attribute")
        print("  unique <attr>           - List unique values with counts")
        print("  sort <attr> <asc|desc>  - Sort data by attribute")
        print("\nData Augmentation:")
        print("  augment <percent> <duplicate|create>")
        print("                          - Increase dataset by percentage")
        print("\nAdvanced Analysis (max 10 penguins):")
        print("  generate research_groups <k>")
        print("                          - Generate groups of k with all species")
        print("  split_into_groups <mass_threshold>")
        print("                          - Split penguins into 2 groups by mass")
        print("\nVisualization:")
        print("  scatter <attr1> <attr2> - Generate scatter plot")
        print("  hist <attr> <bins>      - Generate histogram")
        print("  boxplot <island|species> <attr> - Generate boxplot")
        print("\nMachine Learning (Bonus):")
        print("  classify <culmen_len> <culmen_depth> <flipper_len> <k>")
        print("                          - Predict species using k-NN")
        print("\nFun Commands:")
        print("  random_fact             - Display a random penguin fact")
        print("  draw_penguin            - Display ASCII penguin art")
        print("\nOther:")
        print("  help                    - Show this help menu")
        print("  quit                    - Exit the program")
        print("=" * 60)

    @staticmethod
    def print_quick_commands():
        """Print a compact list of commands"""
        print("\n" + "-" * 75)
        print("Commands: print available_data | load <file> | save_random <k> <file>")
        print("          filter <attr> <val> | describe <attr> | unique <attr>")
        print("          sort <attr> <asc|desc> | augment <pct> <mode>")
        print("          generate research_groups <k> | split_into_groups <mass>")
        print("          scatter | hist | boxplot | classify | random_fact | help | quit")
        print("-" * 75)

    def handle_print_available(self):
        """Handle 'print available_data' command"""
        files = self.__penguin_service.get_available_files()
        if not files:
            print("No CSV files found in data directory.")
            print("Please add CSV files to the 'data' folder.")
        else:
            print(f"\nAvailable CSV files ({len(files)}):")
            for f in files:
                print(f"  - {f}")

    def handle_load(self, filename: str):
        """Handle 'load <filename>' command"""
        try:
            count = self.__penguin_service.load_data(filename)
            print(f"Successfully loaded {count} penguins from '{filename}'")
        except FileNotFoundException as e:
            print(f"Error: {e}")
            print("Use 'print available_data' to see available files.")

    def handle_filter(self, attribute: str, value: str):
        """Handle 'filter <attribute> <value>' command"""
        filtered = self.__penguin_service.filter_data(attribute, value)
        print(f"\nFilter results: {len(filtered)} penguins match the criteria")
        
        if filtered:
            save = input("Do you want to save this data to a new file? (y/n): ").strip().lower()
            if save == 'y':
                filename = input("Enter filename (without extension): ").strip()
                if not filename.endswith('.csv'):
                    filename += '.csv'
                self.__penguin_service.save_filtered_data(filtered, filename)
                print(f"Filtered data saved to '{filename}'")

    def handle_describe(self, attribute: str):
        """Handle 'describe <attribute>' command"""
        stats = self.__penguin_service.describe_attribute(attribute)
        print(f"\nStatistics for '{attribute}':")
        print(f"  Minimum: {stats['min']}")
        print(f"  Maximum: {stats['max']}")
        print(f"  Mean:    {stats['mean']}")

    def handle_unique(self, attribute: str):
        """Handle 'unique <attribute>' command"""
        unique_vals = self.__penguin_service.unique_values(attribute)
        print(f"\nUnique values for '{attribute}':")
        for val, count in sorted(unique_vals.items(), key=lambda x: -x[1]):
            print(f"  {val}: {count} penguins")

    def handle_sort(self, attribute: str, order: str):
        """Handle 'sort <attribute> <asc|desc>' command"""
        sorted_penguins = self.__penguin_service.sort_data(attribute, order)
        print(f"\nData sorted by '{attribute}' in {order}ending order.")
        print(f"Total: {len(sorted_penguins)} penguins")
        print("(Performance logged to sort_performance.log)")
        
        # Show first 5 entries
        print("\nFirst 5 entries:")
        for i, p in enumerate(sorted_penguins[:5]):
            print(f"  {i+1}. {p.get_attribute(attribute)} - {p.get_species()} ({p.get_island()})")

    def handle_augment(self, percent: str, mode: str):
        """Handle 'augment <percent> <duplicate|create>' command"""
        augmented, suggested_filename = self.__penguin_service.augment_data(percent, mode)
        print(f"\nAugmented dataset created: {len(augmented)} penguins")
        
        save = input(f"Save to '{suggested_filename}'? (y/n/custom): ").strip().lower()
        if save == 'y':
            self.__penguin_service.save_augmented_data(augmented, suggested_filename)
            print(f"Saved to '{suggested_filename}'")
        elif save == 'custom':
            filename = input("Enter filename: ").strip()
            if not filename.endswith('.csv'):
                filename += '.csv'
            self.__penguin_service.save_augmented_data(augmented, filename)
            print(f"Saved to '{filename}'")
        else:
            print("Data not saved.")

    def handle_scatter(self, attr1: str, attr2: str):
        """Handle 'scatter <attr1> <attr2>' command"""
        print(f"Generating scatter plot: {attr1} vs {attr2}...")
        self.__stats_service.scatter_plot(attr1, attr2)

    def handle_hist(self, attribute: str, bins: str):
        """Handle 'hist <attribute> <bins>' command"""
        try:
            bins_int = int(bins)
            if bins_int <= 0:
                print("Error: bins must be a positive integer")
                return
        except ValueError:
            print("Error: bins must be a valid integer")
            return
        
        print(f"Generating histogram for {attribute} with {bins_int} bins...")
        self.__stats_service.histogram(attribute, bins_int)

    def handle_boxplot(self, groupby: str, attribute: str):
        """Handle 'boxplot <island|species> <attribute>' command"""
        print(f"Generating boxplot for {attribute} grouped by {groupby}...")
        self.__stats_service.boxplot(groupby, attribute)

    def handle_classify(self, culmen_len: str, culmen_depth: str, flipper_len: str, k: str):
        """Handle 'classify <culmen_len> <culmen_depth> <flipper_len> <k>' command"""
        try:
            cl = float(culmen_len)
            cd = float(culmen_depth)
            fl = float(flipper_len)
            k_val = int(k)
            
            if k_val <= 0:
                print("Error: k must be a positive integer")
                return
                
        except ValueError:
            print("Error: Invalid numeric values provided")
            return
        
        result = self.__classifier_service.classify_with_details(cl, cd, fl, k_val)
        print(f"\n🐧 Classification Result:")
        print(f"  Predicted Species: {result['prediction']}")
        print(f"  Confidence: {result['confidence']}%")
        print(f"  Vote Distribution: {result['votes']}")
        print(f"  k neighbors used: {result['k_used']}")

    def handle_random_fact(self):
        """Handle 'random_fact' command"""
        fact = random.choice(self.__penguin_facts)
        print(f"\n🐧 Penguin Fact: {fact}")

    def handle_save_random(self, k: str, filename: str):
        """Handle 'save_random <k> <filename>' command"""
        try:
            k_val = int(k)
            if k_val <= 0:
                print("Error: k must be a positive integer")
                return
        except ValueError:
            print("Error: k must be a valid integer")
            return
        
        try:
            selected = self.__penguin_service.save_random(k_val, filename)
            print(f"\n✓ Saved {len(selected)} randomly selected penguins to '{filename}'")
            print(f"  Species distribution:")
            species_count = {}
            for p in selected:
                species_count[p.get_species()] = species_count.get(p.get_species(), 0) + 1
            for species, count in species_count.items():
                print(f"    - {species}: {count}")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_generate_research_groups(self, k: str):
        """Handle 'generate research_groups <k>' command"""
        try:
            k_val = int(k)
            if k_val < 3:
                print("Error: k must be at least 3")
                return
        except ValueError:
            print("Error: k must be a valid integer")
            return
        
        try:
            groups = self.__penguin_service.generate_research_groups(k_val)
            if not groups:
                print(f"\nNo valid research groups of size {k_val} found.")
                print("A valid group must have at least one penguin from each species.")
            else:
                print(f"\n🔬 Found {len(groups)} valid research group(s) of size {k_val}:")
                print("-" * 50)
                for i, group in enumerate(groups, 1):
                    print(f"\nGroup {i}:")
                    for p in group:
                        print(f"  - {p.get_species()} ({p.get_island()}, {p.get_sex()}, {p.get_body_mass_g()}g)")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_split_into_groups(self, threshold: str):
        """Handle 'split_into_groups <body_mass_threshold>' command"""
        try:
            threshold_val = float(threshold)
            if threshold_val <= 0:
                print("Error: threshold must be positive")
                return
        except ValueError:
            print("Error: threshold must be a valid number")
            return
        
        try:
            splits = self.__penguin_service.split_into_groups(threshold_val)
            if not splits:
                print(f"\nNo valid splits found with mass threshold {threshold_val}g.")
                print("Each group needs at least 2 penguins and total mass <= threshold.")
            else:
                print(f"\n✂️ Found {len(splits)} valid way(s) to split penguins:")
                print(f"   (Each group has ≥2 penguins and total mass ≤ {threshold_val}g)")
                print("-" * 60)
                for i, (g1, g2) in enumerate(splits, 1):
                    mass1 = sum(p.get_body_mass_g() for p in g1)
                    mass2 = sum(p.get_body_mass_g() for p in g2)
                    print(f"\nSplit {i}:")
                    print(f"  Group A ({len(g1)} penguins, total mass: {mass1}g):")
                    for p in g1:
                        print(f"    - {p.get_species()} ({p.get_body_mass_g()}g)")
                    print(f"  Group B ({len(g2)} penguins, total mass: {mass2}g):")
                    for p in g2:
                        print(f"    - {p.get_species()} ({p.get_body_mass_g()}g)")
        except ValueError as e:
            print(f"Error: {e}")

    @staticmethod
    def handle_draw_penguin():
        """Handle 'draw_penguin' command"""
        penguin_art = r"""
           .--.
          |o_o |
          |:_/ |
         //   \ \
        (|     | )
       /'\_   _/`\
       \___)=(___/
        """
        print(penguin_art)
        print("  A cute penguin for you! 🐧")

    def run(self):
        """Main application loop"""
        print("\n" + "=" * 60)
        print("  Welcome to the PENGUIN DATA ANALYZER")
        print("=" * 60)
        self.print_menu()

        while True:
            try:
                self.print_quick_commands()
                user_input = input("\n> ").strip()
                if not user_input:
                    continue

                parts = user_input.split()
                command = parts[0].lower()

                if command == 'quit':
                    print("Goodbye! 🐧")
                    break

                elif command == 'help':
                    self.print_menu()

                elif command == 'print':
                    if len(parts) >= 2 and parts[1].lower() == 'available_data':
                        self.handle_print_available()
                    else:
                        print("Usage: print available_data")

                elif command == 'load':
                    if len(parts) < 2:
                        print("Usage: load <filename>")
                    else:
                        self.handle_load(parts[1])

                elif command == 'save_random':
                    if len(parts) < 3:
                        print("Usage: save_random <k> <filename>")
                    else:
                        self.handle_save_random(parts[1], parts[2])

                elif command == 'generate':
                    if len(parts) >= 3 and parts[1].lower() == 'research_groups':
                        self.handle_generate_research_groups(parts[2])
                    else:
                        print("Usage: generate research_groups <k>")

                elif command == 'split_into_groups':
                    if len(parts) < 2:
                        print("Usage: split_into_groups <body_mass_threshold>")
                    else:
                        self.handle_split_into_groups(parts[1])

                elif command == 'filter':
                    if len(parts) < 3:
                        print("Usage: filter <attribute> <value>")
                    else:
                        self.handle_filter(parts[1], parts[2])

                elif command == 'describe':
                    if len(parts) < 2:
                        print("Usage: describe <attribute>")
                        print(f"Numeric attributes: {', '.join(Penguin.get_numeric_attributes())}")
                    else:
                        self.handle_describe(parts[1])

                elif command == 'unique':
                    if len(parts) < 2:
                        print("Usage: unique <attribute>")
                        print(f"Attributes: {', '.join(Penguin.get_all_attributes())}")
                    else:
                        self.handle_unique(parts[1])

                elif command == 'sort':
                    if len(parts) < 3:
                        print("Usage: sort <attribute> <asc|desc>")
                    else:
                        self.handle_sort(parts[1], parts[2])

                elif command == 'augment':
                    if len(parts) < 3:
                        print("Usage: augment <percent> <duplicate|create>")
                    else:
                        self.handle_augment(parts[1], parts[2])

                elif command == 'scatter':
                    if len(parts) < 3:
                        print("Usage: scatter <attribute1> <attribute2>")
                        print(f"Numeric attributes: {', '.join(Penguin.get_numeric_attributes())}")
                    else:
                        self.handle_scatter(parts[1], parts[2])

                elif command == 'hist':
                    if len(parts) < 3:
                        print("Usage: hist <attribute> <bins>")
                    else:
                        self.handle_hist(parts[1], parts[2])

                elif command == 'boxplot':
                    if len(parts) < 3:
                        print("Usage: boxplot <island|species> <attribute>")
                    else:
                        self.handle_boxplot(parts[1], parts[2])

                elif command == 'classify':
                    if len(parts) < 5:
                        print("Usage: classify <culmen_len> <culmen_depth> <flipper_len> <k>")
                    else:
                        self.handle_classify(parts[1], parts[2], parts[3], parts[4])

                elif command == 'random_fact':
                    self.handle_random_fact()

                elif command == 'draw_penguin':
                    self.handle_draw_penguin()

                else:
                    raise InvalidCommandException(command)

            except PenguinAppException as e:
                print(f"Error: {e}")
            except KeyboardInterrupt:
                print("\nUse 'quit' to exit.")
            except Exception as e:
                print(f"Unexpected error: {e}")
