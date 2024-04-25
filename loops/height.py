student_heights = input().split()
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
number_students = 0
for i in range(0,len(student_heights)):
    total_height += student_heights[i]
    number_students += 1

avg_height = int(total_height/number_students)

print(f"Total Height: {total_height}")
print(f"Number of Students: {number_students}")
print(f"Average Height: {avg_height}")