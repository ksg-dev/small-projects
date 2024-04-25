student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

high_score = 0
for score in student_scores:
    if high_score < score:
        high_score = score
    else:
        pass

print(f"The highest score in the class is: {high_score}")