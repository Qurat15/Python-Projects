import math


def paint_calc(height, width, cover):
  number_of_cans = (height * width)/coverage
  print(f"You'll need {math.ceil(number_of_cans)} cans of paint.")   # math.ceil will roundup the number 1.6 -> 2

test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
