# done We need to create a script that has 3 elipsis for every word
# done Submit to the course!


# Get the input from the user
talk = input("What do you have to yap about? ")

# TODO Split the input into each individual word
newTalk = talk.split()
for word in newTalk:
    print(word, end="...")

print()
