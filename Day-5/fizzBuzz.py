# 5.4 : FizzBuzz 

fizzBuzz_list = []
num = int(input("When will this last: "))

for i in range(1, num+1):
    if (i % 5 == 0 and i % 3 == 0):
        fizzBuzz_list.append("FizzBuzz")
    elif(i % 3 == 0):
        fizzBuzz_list.append("fizz")
    elif(i % 5 == 0):
        fizzBuzz_list.append("buzz")
    else:
        fizzBuzz_list.append(i)
    
print(fizzBuzz_list)