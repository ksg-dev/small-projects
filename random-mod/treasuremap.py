line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Enter coordinates: ")


cols = ["A", "B", "C"]

second = cols.index(position[0])
first = int(position[1]) - 1

map[first][second] = "X"



print(f"{line1}\n{line2}\n{line3}")