import random
from images_ascii import rock,paper,scissor
game_img = [rock, paper, scissor]
choose = int(input("Type 0 for Rock, 1 for Paper or 2 fo Scissor\n"))
print("You choose: ")
print(game_img[choose])

randChoose = random.randint(0,2)
print("Computer Choose: ")
print(game_img[randChoose])

win = None
if(choose == randChoose):
    win = "Draw"
elif (choose == 0 and randChoose == 2):
    win = "You win"
elif (choose == 0 and randChoose == 1):
    win = "computer win"
elif (choose == 1 and randChoose == 0):
    win = "You win"
elif (choose == 1 and randChoose == 2):
    win = "Computer Win"
elif (choose == 2 and randChoose == 0):
    win = "Computer Win"
elif (choose == 2 and randChoose == 1):
    win = "You Win"
else:
    print("You Lose. Type valid input")
print(win)