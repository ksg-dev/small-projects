# use w file1 and file2
# create list called result that contains shared numbers

# output should be list of integers

# Read file1 into list of numbers
with open("file1.txt") as f1:
    f1_str = f1.readlines()
    f1_list = [int(num.strip()) for num in f1_str]

# Read file2 into list of numbers
with open("file2.txt") as f2:
    f2_str = f2.readlines()
    f2_list = [int(num.strip()) for num in f2_str]

results = [number for number in f1_list if number in f2_list]
print(results)

