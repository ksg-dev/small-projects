from math import ceil

def paint_calc(height, width, cover):
    check = (height * width) / cover
    num_cans = ceil(check)
    print(f"You'll need {num_cans} can(s) of paint.")

test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage) 