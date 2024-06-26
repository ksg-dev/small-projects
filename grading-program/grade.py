student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Neville": 62,
}


student_grades = {}

for student, score in student_scores.copy().items():
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


print(student_grades)

