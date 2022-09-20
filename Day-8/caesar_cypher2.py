# Day - 9 : Caesar Cipher
import string
alphabet = string.ascii_lowercase

def caeser (dir, text_is, shift_by):
    text_answer = ''

    if dir == 'encode': 
            for i in text_is:
                if i in alphabet:
                    text_answer += alphabet[(alphabet.index(i) + shift_by) % len(alphabet)]
                else:
                    text_answer += i
            print(f"The encoded text is \"{text_answer}\"")
    elif dir == "decode":
            for i in text_is:
                if i in alphabet:
                    text_answer += alphabet[(alphabet.index(i) - shift_by) % len(alphabet)]
                else:
                    text_answer += i
            print(f"The decoded text is \"{text_answer}\"")   

while True:
    direction = input("Type 'encode' to encrypt and type 'decode' to decrypt\n").lower()
    text = input("type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        caeser(direction, text, shift)
    elif direction == "decode":
        caeser(direction, text, shift)
    else:
        print("Type Valid input")    

    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if again == 'no':
        print("GOODBYE!")
        break
    elif again == 'yes':
        pass
