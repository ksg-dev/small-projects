def add(*args):
    summ = 0
    for n in args:
        summ += n
    return summ


print(add(1, 2, 3, 4, 5, 6))
