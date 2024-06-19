# Take in an input from the user and remove all the vowels in the string:

user_string = input("Input: ")

# Make the string lowercase so I don't need to type extra stuff:
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

# Iterate over all the letters inside of the user's string:
for letter in user_string:
    if letter in vowels:
        user_string = user_string.replace(letter, "")

print(f"Output: {user_string}")
