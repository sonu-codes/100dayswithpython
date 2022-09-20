# Calculator v1
from calc_ascii import calc_pic
from os import system

# operators function
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculator():
    print(calc_pic)
    n1 = float(input("First number:\t"))
    flag = True
    while flag:
        operator_choice = input("Select an operator (+, -, *, /): ")
        n2 = float(input("Next number:\t"))

        # Operator dictonary
        operator_dict = {
            "+" : add,
            "-" : sub,
            "*" : multiply,
            "/" : divide,
        }

        select_operator_value = operator_dict[operator_choice]
        answer = select_operator_value(n1,n2)
        print(f"{n1} {operator_choice} {n2} = {answer}")

        print(f"Type 'y' to continue calculating with {answer}. or \nType 'q' to quit or \nType 'n' to continue with new calculator. : ")

        again = input().lower()
        if again == "y":
            n1 = answer
        elif again == "n":
            flag = False
            system('cls')
            print("New calculator")

            # Call a function inside a function called recursion
            calculator()
        else:
            print("Calculator closed")
            break

calculator()


