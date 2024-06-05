import random
# keyword breakdown for dict comprehension w list/range
new_dict = {new_key : new_value for item in list}

# keyword breakdown for DC w another dict
new_dict = {new_key : new_value for (key, value) in dict.items()}

# goal, loop through list of names and output dict where
# keys are names from list, and score is random int from 0-100

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# using this template
student_scores = {new_key : new_value for item in list}

# with keywords used
student_scores = {student:random.randint(1,100) for student in names}

# keyword breakdown for DC w another dict - conditional
new_dict = {new_key : new_value for (key, value) in dict.items() if test}

# now loop through student scores - add those that scored above 60 to new dict
passed_students = {student: score for (student, score) in student_scores.items() if score > 60}