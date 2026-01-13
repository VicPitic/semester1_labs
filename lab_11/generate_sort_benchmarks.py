"""
Generate Sort Benchmarks
Creates datasets of various sizes and logs sorting performance
Run this script to populate sort_performance.log with required benchmarks
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from repository.penguin_repo import PenguinRepo
from repository.penguin_repo_file import PenguinRepoFile
from service.penguin_service import PenguinService


def generate_benchmarks():
    """Generate sort benchmarks for various dataset sizes"""
    
    # Initialize services
    repo = PenguinRepo()
    repo_file = PenguinRepoFile("data")
    service = PenguinService(repo, repo_file)
    
    # Load base data
    print("Loading base dataset...")
    count = service.load_data("penguins.csv")
    print(f"Loaded {count} penguins\n")
    
    print("=" * 60)
    print("GENERATING SORT BENCHMARKS")
    print("=" * 60)
    
    # Benchmark 1: Less than 100 penguins (filter to get subset)
    print("\n1. Testing with < 100 penguins...")
    service.load_data("penguins.csv")
    # Filter to get Chinstrap only (~68 penguins)
    filtered = service.filter_data("species", "Chinstrap")
    # Save and reload
    service.save_filtered_data(filtered, "benchmark_small.csv")
    service.load_data("benchmark_small.csv")
    print(f"   Dataset size: {service.get_penguin_count()}")
    service.sort_data("body_mass_g", "asc")
    print("   ✓ Sort completed and logged")
    
    # Benchmark 2: 500-1000 penguins
    print("\n2. Testing with 500-1000 penguins...")
    service.load_data("penguins.csv")
    augmented, filename = service.augment_data(150, "duplicate")
    service.save_augmented_data(augmented, "benchmark_500_1000.csv")
    service.load_data("benchmark_500_1000.csv")
    print(f"   Dataset size: {service.get_penguin_count()}")
    service.sort_data("flipper_length_mm", "desc")
    print("   ✓ Sort completed and logged")
    
    # Benchmark 3: 1000-2000 penguins
    print("\n3. Testing with 1000-2000 penguins...")
    service.load_data("penguins.csv")
    augmented, filename = service.augment_data(350, "create")
    service.save_augmented_data(augmented, "benchmark_1000_2000.csv")
    service.load_data("benchmark_1000_2000.csv")
    print(f"   Dataset size: {service.get_penguin_count()}")
    service.sort_data("culmen_length_mm", "asc")
    print("   ✓ Sort completed and logged")
    
    # Benchmark 4: 5000-10000 penguins
    print("\n4. Testing with 5000-10000 penguins...")
    service.load_data("penguins.csv")
    augmented, filename = service.augment_data(2000, "duplicate")
    service.save_augmented_data(augmented, "benchmark_5000_10000.csv")
    service.load_data("benchmark_5000_10000.csv")
    print(f"   Dataset size: {service.get_penguin_count()}")
    service.sort_data("body_mass_g", "desc")
    print("   ✓ Sort completed and logged")
    
    # Benchmark 5: > 10000 penguins
    print("\n5. Testing with > 10000 penguins...")
    service.load_data("penguins.csv")
    augmented, filename = service.augment_data(3500, "create")
    service.save_augmented_data(augmented, "benchmark_10000_plus.csv")
    service.load_data("benchmark_10000_plus.csv")
    print(f"   Dataset size: {service.get_penguin_count()}")
    service.sort_data("culmen_depth_mm", "asc")
    print("   ✓ Sort completed and logged")
    
    print("\n" + "=" * 60)
    print("BENCHMARKS COMPLETE")
    print("=" * 60)
    
    # Display log file contents
    print("\nSort Performance Log (sort_performance.log):")
    print("-" * 60)
    try:
        with open("sort_performance.log", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Log file not found!")
    
    # Cleanup benchmark files
    print("\nCleaning up benchmark files...")
    benchmark_files = [
        "data/benchmark_small.csv",
        "data/benchmark_500_1000.csv", 
        "data/benchmark_1000_2000.csv",
        "data/benchmark_5000_10000.csv",
        "data/benchmark_10000_plus.csv"
    ]
    for f in benchmark_files:
        try:
            os.remove(f)
            print(f"  Deleted {f}")
        except FileNotFoundError:
            pass
    print("Cleanup complete!")


if __name__ == "__main__":
    generate_benchmarks()
