# 9.1 : Grading Program
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62,
}

#Create an empty dictionary called students_grades.
students_grades = {}

#Add the grades to students_grades.
for key in student_scores:
    score = student_scores[key]
    if score >= 91:
        students_grades[key] = "A"
    elif score >= 81:
        students_grades[key] = "B"
    elif score >= 71:
        students_grades[key] = "C"
    elif score >=61:
        students_grades[key] = "D"
    else:
        students_grades[key] = "F"

print(students_grades)



    
