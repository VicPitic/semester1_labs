# Penguin Data Analyzer - Documentation

## Problem Statement
The research community needs a comprehensive application to analyze penguin datasets from field studies. The application should support data loading, filtering, statistical analysis, visualization, and machine learning classification. The system must handle CSV data files, provide data preprocessing capabilities, and offer both basic statistical operations and advanced features like k-NN classification for species prediction.

## Iteration Plan

### Iteration 1: Core Domain & Data Management (Week 11)
**Goal:** Implement the foundational architecture and basic data operations for penguin dataset analysis.

**Features:**
1. **Data Loading**: Load penguin data from CSV files with preprocessing capabilities.
2. **Domain Model**: Represent penguin entities with all relevant attributes (species, measurements, location).
3. **Basic Operations**: Filter, describe, and explore loaded datasets.
4. **Data Validation**: Ensure data integrity and handle missing values during preprocessing.

**Technical Tasks:**
* Define `Penguin` entity with measurements (flipper length, culmen dimensions, body mass).
* Implement `PenguinValidator` for data validation.
* Implement `PenguinRepo` (In-Memory) and `PenguinRepoFile` for CSV operations.
* Implement `PenguinService` with basic analysis functions.
* Create Console UI with command-line interface.
* Setup preprocessing pipeline for raw CSV data.

### Iteration 2: Statistical Analysis & Data Manipulation (Week 11-12)
**Goal:** Add comprehensive statistical analysis capabilities and data manipulation features.

**Features:**
1. **Statistical Operations**: Calculate min, max, mean for numeric attributes.
2. **Data Exploration**: Find unique values and their frequencies.
3. **Sorting**: Sort data by any attribute with performance logging.
4. **Data Augmentation**: Increase dataset size through duplication or synthetic data creation.
5. **Advanced Grouping**: Generate research groups and split data by thresholds.

**Technical Tasks:**
* Implement statistical calculations in `PenguinService`.
* Add sorting algorithms with time complexity analysis.
* Implement data augmentation strategies (duplicate/create modes).
* Add grouping algorithms for research purposes.
* Performance logging for sorting operations.

### Iteration 3: Visualization & Machine Learning (Week 12)
**Goal:** Implement data visualization and machine learning capabilities for advanced analysis.

**Features:**
1. **Data Visualization**: Generate scatter plots, histograms, and boxplots using matplotlib.
2. **k-NN Classification**: Predict penguin species based on physical measurements.
3. **Interactive Features**: Random penguin facts and ASCII art for user engagement.
4. **Comprehensive Testing**: Unit tests for all components with edge case handling.

**Technical Tasks:**
* Implement `StatsService` for matplotlib visualizations.
* Implement `ClassifierService` with k-NN algorithm.
* Add distance calculation and majority voting logic.
* Create comprehensive test suite covering all functionality.
* Add fun interactive elements for user experience.

---

## Specifications (Iterations 1-3)

### Domain
* **Penguin**: `species` (string), `flipper_length_mm` (float), `culmen_length_mm` (float), `culmen_depth_mm` (float), `body_mass_g` (float), `island` (string), `sex` (string).

### Services
* **PenguinService**:
  * `load_data(filename)` - Load penguins from CSV file
  * `preprocess_data(input_file, output_file)` - Clean and validate raw data
  * `filter_penguins(attribute, value)` - Filter by attribute (numeric: >, string: ==)
  * `describe_attribute(attribute)` - Statistical summary (min, max, mean)
  * `get_unique_values(attribute)` - Unique values with counts
  * `sort_penguins(attribute, order)` - Sort by attribute with performance logging
  * `augment_data(percentage, mode)` - Increase dataset size
  * `generate_research_groups(group_size)` - Create diverse research groups
  * `split_into_groups(threshold)` - Split by mass threshold
  * `save_random_penguins(count, filename)` - Export random sample

* **StatsService**:
  * `generate_scatter_plot(attr1, attr2)` - Create scatter plot visualization
  * `generate_histogram(attribute, bins)` - Create histogram
  * `generate_boxplot(group_by, attribute)` - Create grouped boxplot

* **ClassifierService**:
  * `classify_species(culmen_length, culmen_depth, flipper_length, k)` - k-NN classification
  * `_calculate_distance(penguin1, penguin2)` - Euclidean distance calculation
  * `_get_majority_vote(neighbors)` - Majority voting for prediction

### Repositories
* **PenguinRepo**: In-memory storage with `add`, `add_all`, `get_all_penguins`, `clear`, `get_count`.
* **PenguinRepoFile**: File-based operations with `load_from_file`, `save_to_file`, `get_available_files`.

### Data Flow
1. **Preprocessing**: Raw CSV → Validated CSV (handles missing values, data type conversion)
2. **Loading**: CSV → In-memory penguin objects
3. **Analysis**: Statistical operations on loaded data
4. **Visualization**: Generate plots saved as PNG files
5. **Classification**: k-NN prediction using penguin measurements

## Algorithm Complexities

### Core Operations
* **filter**: O(n) time, O(k) space where k is number of matching penguins
* **describe**: O(n) time, O(1) space
* **unique**: O(n) time, O(k) space where k is number of unique values
* **sort (Insertion Sort)**: O(n²) time, O(1) space (in-place)

### Advanced Operations
* **k-NN Classification**: O(n×k) time where n is dataset size, k is number of neighbors
* **Distance Calculation**: O(d) time where d is number of dimensions (3 for measurements)
* **Augmentation**: O(n×p) time where p is augmentation percentage

## File Structure & Architecture

```
domain/           # Business entities and validation
├── penguin.py    # Penguin entity with measurements
├── validation.py # Data validation rules
└── exceptions.py # Custom exceptions

repository/       # Data access layer
├── penguin_repo.py      # In-memory storage
└── penguin_repo_file.py # CSV file operations

service/          # Business logic layer
├── penguin_service.py     # Core analysis operations
├── stats_service.py       # Visualization service
└── classifier_service.py  # k-NN classification

ui/               # User interface
└── console.py    # Command-line interface

data/             # CSV data files
├── penguins.csv      # Raw data (optional)
└── penguins_data.csv # Preprocessed data
```

## Error Handling
The application includes comprehensive exception handling:
* **NoDataLoadedException**: When operations are attempted without loaded data
* **FileNotFoundException**: When CSV files are not found
* **InvalidAttributeException**: When invalid attributes are specified
* **NonNumericAttributeException**: When numeric operations are attempted on string attributes
* **InvalidFilterValueException**: When filter values cannot be converted to appropriate types
* **InvalidSortOrderException**: When invalid sort orders are provided
* **EmptyDatasetException**: When operations require data but dataset is empty

## Testing Strategy
The application includes comprehensive unit tests:
* **Domain Tests**: Penguin entity, validation rules
* **Repository Tests**: In-memory and file operations, data loading/saving
* **Service Tests**: All analysis operations, edge cases, error conditions
* **Integration Tests**: End-to-end command processing

Test coverage includes:
* Normal operation scenarios
* Edge cases (empty datasets, invalid inputs)
* Error conditions and exception handling
* Performance verification for sorting operations