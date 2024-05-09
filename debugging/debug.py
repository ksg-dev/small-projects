############DEBUGGING#####################

# # Describe Problem - range goes to 19 - have to change range to 21 to include 20
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# # Change range to stay within index
# dice_num = randint(0, 5)
# #dice_num = 6
# print(dice_imgs[dice_num])

# # Play Computer - another range problem
# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# # Just added = to catch 1994
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors - f string
# age = input("How old are you?")
# if age > 18:
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# # remove ==, replace w =
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger - fix indentation so append is inside for loop
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])