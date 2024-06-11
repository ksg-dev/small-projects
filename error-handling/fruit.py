fruits = eval(input())


# TODO Catch the exception and make sure the code runs without crashing
# if index out of range, just put "fruit"
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        fruit = "fruit"
    finally:
        print(fruit + " pie")


make_pie(2)
