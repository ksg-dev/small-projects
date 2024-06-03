PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as n:
    names = n.readlines()


with open("./Input/Letters/starting_letter.txt") as f:
    content = f.read()
    for name in names:
        s_name = name.strip()
        new_letter = content.replace(PLACEHOLDER, s_name)
        with open(f"./Output/ReadyToSend/letter_for_{s_name}.txt", "w") as file:
            file.write(new_letter)
