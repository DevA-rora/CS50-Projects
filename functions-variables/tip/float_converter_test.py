# Takes in the string "VALUE" and turns it into a float

VALUE = "10.69420"
VALUE = float(VALUE)

print(VALUE)
print(type(VALUE))

# Strips the ANOTHER_VALUE of the Dollar sign ($) before converting it into a float data type
ANOTHER_VALUE = "$69.9240"
ANOTHER_VALUE = ANOTHER_VALUE.strip("$")
ANOTHER_VALUE = float(ANOTHER_VALUE)

print(ANOTHER_VALUE)
print(type(ANOTHER_VALUE))


# user_value = input("Give me some money in dollars boy! ")
# user_value = user_value.strip("$")
# user_value = float(user_value)

# print(user_value)
# print(type(user_value))


def dollars_to_float(d):
    # Take in a string (d) and convert it from dollars ($10.00) to a float (10.00)
    d = d.strip("$")
    d = float(d)
    return d


print(dollars_to_float("$10.00"))
