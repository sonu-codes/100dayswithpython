# Prime number check

def prime_num(number):
    prime =""
    for i in range(2, number):
        if number % i == 0:
            prime = f"{number} is divisible by {i} so {number} is not a prime number."
            break
        else:
            prime = f"{number} is a prime number."
    print(prime)

while True:
    num = int(input("Check a prime number: "))
    prime_num(num)
    again = input("Type 'yes' to continue or type 'no' to exit:\n")
    if again == "no":
        break