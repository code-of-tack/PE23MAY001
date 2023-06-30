def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Display welcome message
print("Welcome to CalcPro Factorial Calculation!")

# Prompt user to enter the number
print("Please enter the number for which you want to calculate the factorial:")

# Read the number from the user
number = int(input())

# Calculate the factorial
result = factorial(number)

# Display the result
print("Thank you for providing the number for factorial calculation.")
print(f"The factorial of {number} is: {result}")