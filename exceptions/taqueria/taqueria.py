yummy_food = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

while True:
    try:
        print("woa")
    except EOFError:
        print("EOFError")


# Ask the user for their item. Capitalize every single word in the item.
item = input("Item: ").title()
print(item)

print(yummy_food[item])