#!/usr/bin/env python3
"""
Boilerplate Generator for Layered Architecture Projects
Generates a project structure with domain, repository, service, and UI layers.
"""

import os
import argparse


def create_domain_file(entity_name: str, attributes: list[tuple[str, str]]) -> str:
    """Generate domain class content."""
    # Build __init__ parameters
    params = ", ".join([f"{name}" for name, _ in attributes])
    
    # Build __init__ body
    init_body = "\n".join([f"        self.{name} = {name}" for name, _ in attributes])
    
    # Build __str__ representation
    str_parts = ", ".join([f'{name.capitalize()}: {{self.{name}}}' for name, _ in attributes])
    
    return f'''class {entity_name}:
    def __init__(self, {params}):
{init_body}

    def __str__(self):
        return f"{str_parts}"
    
    def __repr__(self):
        return self.__str__()
'''


def create_repo_file(entity_name: str, attributes: list[tuple[str, str]], data_file: str) -> str:
    """Generate repository class content."""
    entity_lower = entity_name.lower()
    entity_plural = entity_lower + "s"
    
    # Build parsing logic based on attributes
    attr_names = ", ".join([name for name, _ in attributes])
    
    # Build type conversion for parsing
    parse_conversions = []
    for name, type_hint in attributes:
        if type_hint == "int":
            parse_conversions.append(f"int({name})")
        elif type_hint == "float":
            parse_conversions.append(f"float({name})")
        else:
            parse_conversions.append(name)
    
    parse_args = ", ".join(parse_conversions)
    
    # Build save format
    save_attrs = ", ".join([f"{{{entity_lower}.{name}}}" for name, _ in attributes])
    
    return f'''from domain import {entity_name}


class {entity_name}Repository:
    def __init__(self, filename: str):
        self._filename = filename
        self._{entity_plural}: list[{entity_name}] = []
        self._load()

    def _load(self):
        """Load {entity_plural} from file."""
        self._{entity_plural} = []
        try:
            with open(self._filename, "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    {attr_names} = line.split(",")
                    {entity_lower} = {entity_name}({parse_args})
                    self._{entity_plural}.append({entity_lower})
        except FileNotFoundError:
            # File doesn't exist yet, start with empty list
            pass

    def _save(self):
        """Save {entity_plural} to file."""
        with open(self._filename, "w") as file:
            for {entity_lower} in self._{entity_plural}:
                file.write(f"{save_attrs}\\n")

    def add(self, {entity_lower}: {entity_name}):
        """Add a new {entity_lower}."""
        self._load()
        self._{entity_plural}.append({entity_lower})
        self._save()

    def get_all(self) -> list[{entity_name}]:
        """Get all {entity_plural}."""
        self._load()
        return self._{entity_plural}

    def find_by_id(self, id) -> {entity_name} | None:
        """Find a {entity_lower} by ID."""
        self._load()
        for {entity_lower} in self._{entity_plural}:
            if {entity_lower}.id == id:
                return {entity_lower}
        return None

    def update(self, updated_{entity_lower}: {entity_name}):
        """Update an existing {entity_lower}."""
        self._load()
        for i, {entity_lower} in enumerate(self._{entity_plural}):
            if {entity_lower}.id == updated_{entity_lower}.id:
                self._{entity_plural}[i] = updated_{entity_lower}
                self._save()
                return
        raise ValueError(f"{entity_name} with ID {{updated_{entity_lower}.id}} not found")

    def delete(self, id):
        """Delete a {entity_lower} by ID."""
        self._load()
        for i, {entity_lower} in enumerate(self._{entity_plural}):
            if {entity_lower}.id == id:
                del self._{entity_plural}[i]
                self._save()
                return
        raise ValueError(f"{entity_name} with ID {{id}} not found")
'''


def create_service_file(entity_name: str, attributes: list[tuple[str, str]]) -> str:
    """Generate service class content."""
    entity_lower = entity_name.lower()
    
    # Build add method parameters
    params = ", ".join([f"{name}" for name, _ in attributes])
    
    return f'''from domain import {entity_name}


class {entity_name}Service:
    def __init__(self, repository):
        self._repository = repository

    def add_{entity_lower}(self, {params}):
        """Add a new {entity_lower}."""
        {entity_lower} = {entity_name}({params})
        self._repository.add({entity_lower})

    def get_all_{entity_lower}s(self):
        """Get all {entity_lower}s."""
        return self._repository.get_all()

    def find_{entity_lower}_by_id(self, id):
        """Find a {entity_lower} by ID."""
        {entity_lower} = self._repository.find_by_id(id)
        if {entity_lower} is None:
            raise ValueError(f"{entity_name} with ID {{id}} not found")
        return {entity_lower}

    def update_{entity_lower}(self, {params}):
        """Update an existing {entity_lower}."""
        {entity_lower} = {entity_name}({params})
        self._repository.update({entity_lower})

    def delete_{entity_lower}(self, id):
        """Delete a {entity_lower} by ID."""
        self._repository.delete(id)

    # TODO: Add your custom business logic methods here
'''


def create_ui_file(entity_name: str, attributes: list[tuple[str, str]]) -> str:
    """Generate console UI class content."""
    entity_lower = entity_name.lower()
    
    # Build input prompts for add operation
    input_prompts = []
    for name, type_hint in attributes:
        prompt_text = f'input("Enter {entity_lower} {name}: ")'
        if type_hint == "int":
            input_prompts.append(f'        {name} = int({prompt_text})')
        elif type_hint == "float":
            input_prompts.append(f'        {name} = float({prompt_text})')
        else:
            input_prompts.append(f'        {name} = {prompt_text}')
    
    input_section = "\n".join(input_prompts)
    add_params = ", ".join([name for name, _ in attributes])
    
    return f'''class ConsoleUI:
    def __init__(self, service):
        self._service = service

    def _print_menu(self):
        print("\\n" + "=" * 40)
        print(f"  {entity_name} Management System")
        print("=" * 40)
        print("1. Add {entity_name}")
        print("2. View All {entity_name}s")
        print("3. Find {entity_name} by ID")
        print("4. Update {entity_name}")
        print("5. Delete {entity_name}")
        print("0. Exit")
        print("=" * 40)

    def run(self):
        while True:
            self._print_menu()
            choice = input("Choose an option: ").strip()

            try:
                if choice == "1":
                    self._add_{entity_lower}()
                elif choice == "2":
                    self._view_all_{entity_lower}s()
                elif choice == "3":
                    self._find_{entity_lower}_by_id()
                elif choice == "4":
                    self._update_{entity_lower}()
                elif choice == "5":
                    self._delete_{entity_lower}()
                elif choice == "0":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid option. Please try again.")
            except ValueError as e:
                print(f"Error: {{e}}")
            except Exception as e:
                print(f"An unexpected error occurred: {{e}}")

    def _add_{entity_lower}(self):
{input_section}
        self._service.add_{entity_lower}({add_params})
        print("{entity_name} added successfully!")

    def _view_all_{entity_lower}s(self):
        {entity_lower}s = self._service.get_all_{entity_lower}s()
        if not {entity_lower}s:
            print("No {entity_lower}s found.")
            return
        print(f"\\nAll {entity_name}s:")
        print("-" * 40)
        for {entity_lower} in {entity_lower}s:
            print({entity_lower})

    def _find_{entity_lower}_by_id(self):
        id = int(input("Enter {entity_lower} ID: "))
        {entity_lower} = self._service.find_{entity_lower}_by_id(id)
        print(f"\\nFound: {{{entity_lower}}}")

    def _update_{entity_lower}(self):
        print("Enter the updated {entity_lower} details:")
{input_section}
        self._service.update_{entity_lower}({add_params})
        print("{entity_name} updated successfully!")

    def _delete_{entity_lower}(self):
        id = int(input("Enter {entity_lower} ID to delete: "))
        self._service.delete_{entity_lower}(id)
        print("{entity_name} deleted successfully!")
'''


def create_main_file(entity_name: str, data_file: str) -> str:
    """Generate main.py content."""
    return f'''from repo import {entity_name}Repository
from service import {entity_name}Service
from ui import ConsoleUI


def main():
    repository = {entity_name}Repository("{data_file}")
    service = {entity_name}Service(repository)
    ui = ConsoleUI(service)
    ui.run()


if __name__ == "__main__":
    main()
'''


def create_data_file(attributes: list[tuple[str, str]]) -> str:
    """Generate sample data file content."""
    # Create a sample entry
    sample_values = []
    for i, (name, type_hint) in enumerate(attributes):
        if name.lower() == "id":
            sample_values.append("1")
        elif type_hint == "int":
            sample_values.append("10")
        elif type_hint == "float":
            sample_values.append("99.99")
        else:
            sample_values.append(f"Sample{name.capitalize()}")
    
    return ",".join(sample_values) + "\n"


def parse_attributes(attr_string: str) -> list[tuple[str, str]]:
    """Parse attribute string into list of (name, type) tuples.
    
    Format: "name:type,name:type,..." 
    Example: "id:int,name:str,price:float"
    """
    attributes = []
    for attr in attr_string.split(","):
        attr = attr.strip()
        if ":" in attr:
            name, type_hint = attr.split(":", 1)
            attributes.append((name.strip(), type_hint.strip()))
        else:
            # Default to str if no type specified
            attributes.append((attr, "str"))
    return attributes


def create_boilerplate(project_name: str, entity_name: str, attributes: list[tuple[str, str]], base_path: str = "."):
    """Create the complete boilerplate project structure."""
    # Create project directory
    project_path = os.path.join(base_path, project_name)
    os.makedirs(project_path, exist_ok=True)
    
    data_file = f"{entity_name.lower()}s.txt"
    
    # Create all files
    files = {
        "domain.py": create_domain_file(entity_name, attributes),
        "repo.py": create_repo_file(entity_name, attributes, data_file),
        "service.py": create_service_file(entity_name, attributes),
        "ui.py": create_ui_file(entity_name, attributes),
        "main.py": create_main_file(entity_name, data_file),
        data_file: create_data_file(attributes),
    }
    
    for filename, content in files.items():
        filepath = os.path.join(project_path, filename)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Created: {filepath}")
    
    print(f"\n✅ Project '{project_name}' created successfully at {project_path}")
    print(f"\nTo run the project:")
    print(f"  cd {project_path}")
    print(f"  python main.py")


def interactive_mode():
    """Run the generator in interactive mode."""
    print("=" * 50)
    print("  Boilerplate Project Generator")
    print("=" * 50)
    
    project_name = input("\nEnter project/folder name (e.g., 'exam_2'): ").strip()
    if not project_name:
        project_name = "new_project"
    
    entity_name = input("Enter entity name (e.g., 'Product', 'Student'): ").strip()
    if not entity_name:
        entity_name = "Entity"
    
    # Capitalize first letter
    entity_name = entity_name[0].upper() + entity_name[1:]
    
    print("\nEnter attributes in format: name:type (comma-separated)")
    print("Types: int, float, str (default)")
    print("Example: id:int,name:str,brand:str,quantity:int,price:float")
    
    attr_input = input("\nAttributes: ").strip()
    if not attr_input:
        attr_input = "id:int,name:str"
    
    attributes = parse_attributes(attr_input)
    
    print(f"\n📋 Summary:")
    print(f"   Project: {project_name}")
    print(f"   Entity: {entity_name}")
    print(f"   Attributes: {attributes}")
    
    confirm = input("\nProceed? (Y/n): ").strip().lower()
    if confirm in ("", "y", "yes"):
        create_boilerplate(project_name, entity_name, attributes)
    else:
        print("Cancelled.")


def main():
    parser = argparse.ArgumentParser(
        description="Generate boilerplate project with layered architecture (domain, repo, service, ui)"
    )
    parser.add_argument(
        "-n", "--name",
        help="Project/folder name (e.g., 'exam_2')"
    )
    parser.add_argument(
        "-e", "--entity",
        help="Entity name (e.g., 'Product', 'Student')"
    )
    parser.add_argument(
        "-a", "--attributes",
        help="Attributes in format 'name:type,name:type,...' (e.g., 'id:int,name:str,price:float')"
    )
    parser.add_argument(
        "-p", "--path",
        default=".",
        help="Base path where project folder will be created (default: current directory)"
    )
    parser.add_argument(
        "-i", "--interactive",
        action="store_true",
        help="Run in interactive mode"
    )
    
    args = parser.parse_args()
    
    # If no arguments provided or interactive flag, run interactive mode
    if args.interactive or (not args.name and not args.entity and not args.attributes):
        interactive_mode()
    else:
        # Command line mode
        if not args.name or not args.entity or not args.attributes:
            print("Error: When using command line mode, --name, --entity, and --attributes are required.")
            print("Use -i for interactive mode or provide all required arguments.")
            return
        
        entity_name = args.entity[0].upper() + args.entity[1:]
        attributes = parse_attributes(args.attributes)
        create_boilerplate(args.name, entity_name, attributes, args.path)


if __name__ == "__main__":
    main()
