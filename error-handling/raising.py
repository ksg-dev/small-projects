# in meters
height = float(input("Height: "))
# in kg
weight = int(input("Weight: "))

# raise error if values are obviously wrong
if height > 3:
    raise ValueError("Human height shouldn't be over 3 meters")

bmi = weight / height ** 2
print(bmi)