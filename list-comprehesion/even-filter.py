list_of_strings = input("input: ").split(',')

# TO DO: Use list comprehension to convert strings to integers
numbers = [int(i) for i in list_of_strings]
print(f"numbers: {numbers}")

# TO DO: Use LC to filter out the odd numbers
# store the even numbers in a list called result
result = [num for num in numbers if num % 2 == 0]

print(f"result: {result}")
