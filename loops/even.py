# Enter a number between 0 and 1000
target = int(input())
total = 0
if 0 < target > 1000:
    print("Number outside range. Please enter a number between 0 and 1000.")
else:
    for i in range(target + 1):
        if i % 2 == 0:
            total += i
        else:
            pass

print(total)
    