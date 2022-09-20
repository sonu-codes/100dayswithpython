# Hangman
import random, string
from hangman_ascii import hangman_art, hangman_pics
print(hangman_art)

alphabet = string.ascii_lowercase

# Random Word list
word_list = ["all","and", "boy","book","call", "children", "city","dog",
"enemy","enough", "father", "friend", "food","hear","house","inside","laugh", "listen",
"never","noice","often","room","smile","speak","water","woman","work"]

#list to string conversion function
def list_to_str (list):
    string = ''
    for i in list:
        string +=i
    return string

# Select a random word from word list
random_word = random.choice(word_list)

#-------------------------
"""
print(random_word)
"""
#-------------------------
# Same blank spaces as word length
display = []
for i in random_word:
    display.append("_")

#Keeping hangman attemts as -1 because list will start with 0
hangman_attempts =-1

#Check upto when while lopp will occur
while list_to_str(display) != random_word:

    #Take input from user
    guess_letter = input("Guess a letter: ").lower()

    #Check if the input is valid or not
    if (guess_letter in alphabet):
        if guess_letter in random_word:

            # # Place the input at the same place it has to be
            for letter in range(len(random_word)):
                if random_word[letter] == guess_letter:
                    display[letter] = random_word[letter]

            print(list_to_str(display))

            # Check if word is complete or not
            if list_to_str(display) == random_word:
                print("You win",list_to_str(display),"is a correct answer")
                break
        else:
            #Increment in the hangman attempts
            hangman_attempts += 1

            #print the word
            print(list_to_str(display))

            #printing the exact image of hangman till now
            print(hangman_pics[hangman_attempts])

            #check if hangman died or not
            if hangman_attempts == len(hangman_pics)-1:
                print("You failed to save a man. Game Over")
                break
            
    else:
        print("Invalid input")  
