# 5.1 : Average Height

# split() will convert the string into list after each space
student_heights = input("Student Height: ").split()

# convert str values into int
for i in range(len(student_heights)):
    student_heights[i] = int(student_heights[i])

sum = 0
count = 0
for j in student_heights:
    sum += j
    count += 1

avg = round(sum / count)
print(student_heights)
print(avg)