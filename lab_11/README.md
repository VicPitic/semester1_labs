# Penguin Data Analyzer

A Python command-line application to manage and analyze penguin datasets.

## Project Structure

```
lab_11/
├── main.py                    # Entry point
├── data/                      # CSV data files directory
│   ├── penguins.csv           # Raw data (optional)
│   └── penguins_data.csv      # Preprocessed data
├── domain/                    # Domain entities
│   ├── penguin.py             # Penguin class
│   ├── exceptions.py          # Custom exceptions
│   └── validation.py          # Validators
├── repository/                # Data access layer
│   ├── penguin_repo.py        # In-memory repository
│   └── penguin_repo_file.py   # File-based repository
├── service/                   # Business logic
│   ├── penguin_service.py     # Core operations (filter, describe, etc.)
│   ├── stats_service.py       # Visualization service
│   └── classifier_service.py  # k-NN classification
├── ui/                        # User interface
│   └── console.py             # CLI interface
└── all_tests/                 # Unit tests
    ├── run_all_tests.py       # Test runner
    ├── test_domain.py         # Domain tests
    ├── test_repo.py           # Repository tests
    └── test_service.py        # Service tests
```

## Usage

### Running the Application
```bash
python main.py
```

### Preprocessing Raw Data
```bash
python main.py --preprocess
```

### Running Tests
```bash
python main.py --test
```

## Available Commands

| Command | Description |
|---------|-------------|
| `print available_data` | List all CSV files in data directory |
| `load <filename>` | Load data from a CSV file |
| `filter <attr> <value>` | Filter data (numeric: >, string: ==) |
| `describe <attr>` | Show min, max, mean for numeric attribute |
| `unique <attr>` | List unique values with counts |
| `sort <attr> <asc\|desc>` | Sort data by attribute |
| `augment <percent> <duplicate\|create>` | Increase dataset size |
| `scatter <attr1> <attr2>` | Generate scatter plot |
| `hist <attr> <bins>` | Generate histogram |
| `boxplot <island\|species> <attr>` | Generate boxplot |
| `classify <cl> <cd> <fl> <k>` | Predict species using k-NN |
| `random_fact` | Display a random penguin fact |
| `draw_penguin` | Display ASCII penguin art |
| `help` | Show available commands |
| `quit` | Exit the program |

## Time & Space Complexity

### filter
- **Time Complexity**: O(n) where n is the number of penguins
- **Space Complexity**: O(k) where k is the number of matching penguins

### describe
- **Time Complexity**: O(n) where n is the number of penguins
- **Space Complexity**: O(1) - only stores min, max, sum, count

### unique
- **Time Complexity**: O(n) where n is the number of penguins
- **Space Complexity**: O(k) where k is the number of unique values

### sort (Insertion Sort)
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1) in-place sorting

## Dependencies

- Python 3.10+
- matplotlib (for visualization)

## Testing

The application includes comprehensive unit tests for:
- Domain layer (Penguin class, validators)
- Repository layer (CRUD operations, filtering)
- Service layer (filter, describe, unique functionalities)

Run tests with:
```bash
python main.py --test
```
