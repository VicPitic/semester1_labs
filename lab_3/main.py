import random

def calculate_control_digit(n):
    n = abs(n)
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def has_even_control_digit(n):
    return calculate_control_digit(n) % 2 == 0

def read_list():
    try:
        input_str = input("Enter numbers: ")
        numbers = list(map(int, input_str.split()))
        return numbers
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
        return None

def generate_random_list():
    try:
        count = int(input("Enter the number of random numbers to generate: "))
        if count <= 0:
            print("Number of elements must be positive.")
            return None
        
        min_val = int(input("Enter the minimum value: "))
        max_val = int(input("Enter the maximum value: "))
        
        if min_val > max_val:
            print("Minimum value cannot be greater than maximum value.")
            return None
        
        numbers = [random.randint(min_val, max_val) for _ in range(count)]
        return numbers
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return None

def is_power_of_2(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

def control_digit_even(n):
    control_digit = calculate_control_digit(n)
    return control_digit % 2 == 0

def find_max_powers_of_2_sublist(numbers):
    if not numbers:
        return []
    
    max_sublist = []
    current_sublist = []
    
    for num in numbers:
        if is_power_of_2(num):
            current_sublist.append(num)
        else:
            if len(current_sublist) > len(max_sublist):
                max_sublist = current_sublist[:]
            current_sublist = []
    
    # Check the last sublist
    if len(current_sublist) > len(max_sublist):
        max_sublist = current_sublist[:]
    
    return max_sublist

def remove_control_digit_even(numbers):
    return [num for num in numbers if not control_digit_even(num)]

def remove_even_control_digit_elements(numbers):
    """Remove elements with even control digits from the list."""
    return [num for num in numbers if not has_even_control_digit(num)]

def print_list(numbers):
    if not numbers:
        print("The list is empty.")
    else:
        print(f"The current list is: {numbers}")

def print_menu():
    print("\n1. Read a list of integer numbers")
    print("2. Generate a list of random numbers")
    print("3. Find sublist with maximum length where all elements are powers of 2.")
    print("4. Remove elements where the control digit of the number is even.")
    print("5. Exit")

def main():
    numbers = []
    
    while True:
        print_menu()
        choice = input("Choose option:\n>> ").strip()
        
        if choice == '1':
            new_numbers = read_list()
            if new_numbers is not None:
                numbers = new_numbers
                print_list(numbers)
        
        elif choice == '2':
            new_numbers = generate_random_list()
            if new_numbers is not None:
                numbers = new_numbers
                print_list(numbers)
        
        elif choice == '3':
            if not numbers:
                print("List is empty. Please read numbers first.")
            else:
                max_sublist = find_max_powers_of_2_sublist(numbers)
                if max_sublist:
                    print(f"Maximum sublist with all powers of 2: {max_sublist}")
                else:
                    print("No sublist found where all elements are powers of 2.")
        
        elif choice == '4':
            if not numbers:
                print("List is empty. Please read numbers first.")
            else:
                numbers = remove_control_digit_even(numbers)
                print_list(numbers)
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

