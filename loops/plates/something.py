# IDEA 💡: Split the string into a list, then make another list that contains only the numbers of the plate, check if the 1st number [0] is a 0.

# GOAL 🎯: Make sure that the plate string "CS50P2" is invalid while keeping correct logic.
plate = "CS50P2"
plate_list = list(plate)
numbers_in_plate_list = []

print(plate)
print(plate_list)


for character in plate_list:
    if character.isdigit() is True:
        numbers_in_plate_list.append(character)
    else:
        pass

print(numbers_in_plate_list)

# Get last element of plate_list:
print(plate_list[-1])

# IDEA 💡: 1st, check if the last digit of a plate is a digit, then check if that digit is connected to other digits before connecting to numbers, if it connects to digits and then numbers, return False.
if plate_list[-1].isdigit() is True:
    # Check if the digit is conecting to other digits before connecting to a letter.
    if plate_list[-2].isdigit() is True:
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")
