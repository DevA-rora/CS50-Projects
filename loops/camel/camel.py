# Get the user's input:
user_string = input("camelCase: ")

for letter in user_string:
    if letter.isupper() is True:
        # do something
        user_string = user_string.replace(letter, f"_{letter.lower()}")

    elif letter.isupper() is False:
        pass
print(f"snakeCase: {user_string}")
