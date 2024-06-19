# A program that takes the user's input as an expression and prints out the result

expression = input("Expression: ")

# Initialize final number as 0 so we can use it later in the program
final_number = 0

"""
Operations:
- Addition
- Subtraction
- Multiplication
- Division
"""

# Remove unnessecary whitespace of expression and split the string into each part:
expression = expression.strip().split()

# Convert strings to floats:
first_number = float(expression[0])
second_number = float(expression[2])

# Check what operation the user used and calculate the expression accordingly

if expression[1] == "+":
    # Add the two number variables together
    final_number = first_number + second_number
elif expression[1] == "-":
    # Subtrack first number and 2nd number
    final_number = first_number - second_number
elif expression[1] == "*":
    # Multiply
    final_number = first_number * second_number
elif expression[1] == "/":
    # Divide
    final_number = first_number / second_number
else:
    print("I'm sorry, I didn't know what you were trying to calculate...")

final_rounded_number = round(final_number, 2)
print(final_rounded_number)
