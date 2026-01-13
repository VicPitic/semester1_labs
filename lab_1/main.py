# Problem a)
a = input("Enter a number: ")
b = input("Enter another number: ")
sum = float(a) + float(b)
print("The sum is:", sum)

#problem b)
n = int(input("Enter a positive integer: "))
p = 1
for i in range(1, n + 1):
    p *= i
print("The product is:", p)

#problem c)

zero_digits = 0
while p % 10 == 0 and p != 0:
    p /= 10
    zero_digits += 1
print("The number of zeros is:", zero_digits)

#problem d)

num = input("Enter a positive integer: ")
is_perfect_number = True
sum_of_divisors = 0
for i in range(1, int(num)):
    if int(num) % i == 0:
        sum_of_divisors += i
if sum_of_divisors != int(num):
    is_perfect_number = False
if is_perfect_number:
    print(num, "is a perfect number")