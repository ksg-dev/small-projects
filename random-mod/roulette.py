import random

def main():
    names = input("Enter list of names separated by comma-space:")
    names_list = names.split(", ")
    length = len(names_list)-1

    winner = random.randint(0,length)

    print(f"{names_list[winner]} is going to buy the meal today!")


main()