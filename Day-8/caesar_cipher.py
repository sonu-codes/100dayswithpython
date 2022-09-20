# Day-8 : Caesar cipher
import string

# Alphabet list
alphabets = string.ascii_lowercase

# Save outputs
encode_result = ''
decode_result = ''

# Loop until the user does'nt want to stop
while (True):

    # Take input about choices
    choice = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
    if(choice == "encode" or choice =="decode"):
        if choice == "encode":
            encode = input("Type to encrypt:\n").lower()
            shifting = int(input("Type the shift number:\n"))

            # loop every letter of encode
            for i in encode:

                # Loop every letter of alphabet
                for j in alphabets:

                    # if encode letter and alphabet letter are same than
                    if i == j : 
                        # Use modulo to get result after alphabet list ends
                        encode_result += alphabets[(alphabets.index(i) + shifting)%26]
            print(encode_result)

        elif choice == "decode":
            decode = input("Type to decrypt:\n").lower()
            shifting = int(input("Type the shift number:\n"))

            # loop every letter of decode
            for i in decode:

                # Loop every letter of alphabet
                for j in alphabets:

                    # if decode letter and alphabet letter are same than
                    if i == j :
                        decode_result += alphabets[(alphabets.index(i) - shifting)%26]
                    
            print(decode_result)
    else:
        print("Invalid values")

    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if again == 'no':
        break
    elif again == 'yes':
        pass

#------------------------------------------------------------
                        # Practise
#------------------------------------------------------------
demo = "a b c"
for i in demo:
    if i == " ":
        print("space")