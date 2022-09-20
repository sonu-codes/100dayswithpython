# 4.2 : Who will pay the bill
import random
print("Who will make today's food.")
names = input("Name list: ").split(", ")
selected = random.randint(0, len(names)-1)
food_by = names[selected]
print(f"Today's food will maked by {food_by.capitalize()}.")