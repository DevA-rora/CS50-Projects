# We need to create a python script that will return a certain value depending on what the user's greeting is.

# Get the input from the user's greeting
greeting = input("Greeting: ")

# Make the greeting lowercase and split the greeting into its indivudual words
greeting = greeting.lower()
greeting_split = greeting.split()


if "hello" in greeting_split[0]:
    print("$0")
elif greeting_split[0][0] == "h":
    print("$20")
else:
    print("$100")


print()
