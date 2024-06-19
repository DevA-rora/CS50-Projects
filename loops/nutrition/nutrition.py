# Get the calories and other nutrition information for a food item:

"""
Fruits:
- Apple
- Avocado
- Banana
- Cantaloupe
- Grapefruit
- Grapes
- Honeydew Melon
- Kiwifruit
- Lemon
- Lime
- Necatarine
- Orange
- Peach
- Pear
- Pineapple
- Plums
- Strawberries
- Sweet Cherries
- Tangarine
- Watermelon
"""
# Initialize a dictionary that contains the fruit and its calories:
fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}


# Ask the user for the fruit. Use the .lower() function so that we don't need to worry about casing:
user_fruit = input("Item: ").lower()

# Rather than use a conditional with 20 different fruits, we can use a dictionary to associate a fruit with its calories:
if user_fruit in fruits:
    print(f"Calories: {fruits[user_fruit]}")
