'''Day-3: Treasure Island'''

print("Welcome to the treasure Island.")
print("Your mission is to find the treasure.")


print('''"You're at a cross road. Where do you want to go(left or right): "''')
leftOrRight = input().lower()

if (leftOrRight == "left"):
    print('''"You come to a lake. There is an island in the middle of a lake. 
    Type \"wait\" to wait for a boat or type \"swim\" to swim across."''')

    waitOrSwim = input().lower()

    if (waitOrSwim == "wait"):
        print('''"You arrived at the island unharmed. There is a house 
        with 3 doors(red,yellow,blue).Choose one: "''')
        
        door = input().lower() 
        if door == "yellow":
            print("You Win")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")