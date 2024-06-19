# Get a file name from the user and print out what extension it has:

# Take user input, make it all lowercase, remove unnessecary spacing using .strip()

file_name = input("File name: ")
file_name = file_name.lower().strip()

# filetypes:
"""
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip

"""


if ".gif" in file_name:
    print("image/gif")
elif ".jpg" in file_name:
    print("image/jpeg")
elif ".jpeg" in file_name:
    print("image/jpeg")
elif ".png" in file_name:
    print("image/png")
elif ".pdf" in file_name:
    print("application/pdf")
elif ".txt" in file_name:
    print("text/plain")
elif ".zip" in file_name:
    print("application/zip")


else:
    print("application/octet-stream")
