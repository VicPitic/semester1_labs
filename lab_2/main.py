#problems: 5, 12, 19, 1

def smallest_number(n):
    digits = []
    n = abs(n)
    while n > 0:
        digits.append(n % 10)
        n //= 10
    
    digits.sort()
    
    # If first digit is 0, swap with first non-zero digit
    if digits[0] == 0:
        for i in range(1, len(digits)):
            if digits[i] != 0:
                digits[0], digits[i] = digits[i], digits[0]
                break
    
    result = 0
    for digit in digits:
        result = result * 10 + digit
    
    return result

def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def divisible_by_digit_sum(a, b):
    numbers = []
    for n in range(a + 1, b):
        if n % digit_sum(n) == 0:
            numbers.append(n)
    return numbers

def sum_divisible_by_k(n, k):
    numbers = []
    for num in range(11, n):
        if digit_sum(num) % k == 0:
            numbers.append(num)
    return numbers

def control_digit(n):
    n = abs(n)
    
    while n >= 10:
        n = digit_sum(n)

    return n

print(control_digit(9279))  # Example usage
# Problem 1: Determine the smallest number that can be formed with the digits of a number read from the keyboard.
n = int(input("Enter a number: "))
result = smallest_number(n)
print(f"Smallest number from digits of {n}: {result}")

# Problem 2: Print all numbers greater than a given number a and smaller than a given number b that are divisible by the sum of their digits.
a = int(input("Enter lower bound a: "))
b = int(input("Enter upper bound b: "))
numbers = divisible_by_digit_sum(a, b)
print(f"Numbers between {a} and {b} divisible by sum of digits: {numbers}")

# Problem 3: Print all the numbers greater than 10 and smaller than a given n that have the sum of their digits divisible by a given k.
# Example: for n = 26, k = 4, the numbers are: 13, 17, 22.
n = int(input("Enter upper bound n: "))
k = int(input("Enter divisor k: "))
numbers = sum_divisible_by_k(n, k)
print(f"Numbers > 10 and < {n} with digit sum divisible by {k}: {numbers}")

# Problem 4: Compute the control digit of an integer by summing up its digits, then summing up the digits of thesum, so on, until a sum of only one digit is obtained.
num = int(input("Enter a number to find its control digit: "))
control = control_digit(num)
print(f"Control digit of {num}: {control}")