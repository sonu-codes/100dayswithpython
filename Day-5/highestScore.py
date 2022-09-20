#5.2 : Highest score in the class

student_score = input("Score of students: ").split()

for i in range(len(student_score)):
    student_score[i] = int(student_score[i])

max_marks = 0
for max in student_score:
    if(max_marks < max):
        max_marks = max

print(max_marks)