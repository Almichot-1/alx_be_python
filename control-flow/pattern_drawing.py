# Drawing Patterns with Nested Loops

# Ask for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop (while): controls the rows
while row < size:
    # Inner loop (for): controls the columns
    for col in range(size):
        print("*", end="")
    print()  # Move to next line after a row
    row += 1
