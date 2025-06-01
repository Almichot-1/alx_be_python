# Multiplication Table Generator

# Ask for user input
number = int(input("Enter a number to see its multiplication table: "))

# Print multiplication table from 1 to 10
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
