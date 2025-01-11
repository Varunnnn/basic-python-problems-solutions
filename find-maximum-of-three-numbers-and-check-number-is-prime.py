"""
Problem Statement : Write a Python function to:
Find the maximum of three numbers.
Check if a number is prime.

Let's do it.

"""

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))

if num1 >= num2 and num1 >= num3:
    print("The greatest number is", num1)
elif num2 >= num1 and num2 >= num3:
    print("The greatest number is", num2)
else:
    print("The greatest number is", num3)

if num3 > 1:
    is_prime = True
    for i in range(2, int(num3**0.5) + 1):
        if num3 % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num3, "is a prime number")
    else:
        print("The number is not prime")
else:
    print(num3, "is not a prime number")
