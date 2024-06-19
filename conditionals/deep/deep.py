# If the user types in 42, forty two, or forty-two, return yes, else return no:

user_input = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? "
)

# Make the case lower case so that making the conditional statements is a bit easier
user_input = user_input.lower().strip()

if user_input == "42":
    print("Yes")
elif user_input == "forty-two":
    print("Yes")
elif user_input == "forty two":
    print("Yes")
else:
    print("No")
