# Read file
with open("myfile.txt") as file:
    contents = file.read()
    print(contents)


# Write to file - replaces all text in file w new text
with open("myfile.txt", mode="w") as file:
    file.write("New text.")

# Write to file - add to existing text
with open("myfile.txt", mode="a") as file:
    # use newline
    file.write("\nJust kidding add this text")
