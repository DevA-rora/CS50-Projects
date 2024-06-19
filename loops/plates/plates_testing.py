# Import string so that we can use the alphabet and punctuation list:
import string

# Initialize the alphabet and punctuation list:
alphabet = list(string.ascii_letters)
punctuation = list(string.punctuation)

# Initialize the numbers list:
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


# Create the main function:
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# Create the is_valid function:
def is_valid(plate):
    # Check if the first two characters of the plate are letters: ✅
    if plate[0:2].isalpha():
        pass
    else:
        return False

    # Check if the plate is between 2 and 6 characters:
    if len(plate) >= 2 and len(plate) <= 6:
        pass
    else:
        return False

    # Check if the plate has a 0 as the first number in the plate:

    # Initialise the plate_list and numbers_in_plate_list:
    plate_list = list(plate)
    numbers_in_plate_list = []

    # Iterate over all characters in plate_list and determine if they are numbers:
    for character in plate_list:
        if character.isdigit() is True:
            # Append the numbers from the plate_list to the numbers_in_plate_list:
            numbers_in_plate_list.append(character)
        else:
            pass

    # Check if the first number in the plate is 0 by checking if the first element in numbers_in_plate_list is 0:
    if numbers_in_plate_list:
        if numbers_in_plate_list[0] == "0":
            return False
        else:
            pass
    else:
        pass

    # Check if the plate has any punctuation:
    for character in plate:
        if character in punctuation:
            return False
        else:
            pass

    # Check if there are any numbers in the middle of the plate:

    # Check if the last character of the plate is a digit:
    if numbers_in_plate_list:
        if plate_list[-1].isdigit() is True:
            # Check if the last digit is connected to other digits before connecting to a letter:
            if plate_list[-2].isdigit() is False:
                if numbers_in_plate_list:
                    return False
                else:
                    pass
                
    # If all the conditions are met, return True:
    return True


# Testing:
print(is_valid("CS50"))
print(is_valid("CS05"))
print(is_valid("CS50P"))
print(is_valid("PI3.14"))
print(is_valid("H"))
print(is_valid("OUTATIME"))

# Run the program:
main()
"""
Code Criteria:
- [✅] “All vanity plates must start with at least two letters.”
- [✅] “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
- [😑] “Numbers cannot be used in the middle of a plate; they must come at the end. 
    - [😑] For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 

- [✅] "The first number used cannot be a ‘0’.”
- [✅] “No periods, spaces, or punctuation marks are allowed.”
- [ ] "Clean up the code and add comments as needed."
"""
