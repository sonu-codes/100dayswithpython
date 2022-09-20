# Day-8.1 : Area calculate
import math


def areaCalc (height, width, coverage):
    no_of_can = math.ceil((height * width) / coverage)
    print(f"You'll need {no_of_can} cans of paint.")

height = int(input("Height of the wall: "))
width = int(input("Width of the wall: "))
coverance = 5

areaCalc(height, width,coverance)