student = {"name": "Solimar", "grade": "87", "subjects": ["Geometry", "Geography", "Literature"]}

for item in student:
    print(f"{item}: {student[item]}")

student["graduated"] = False

print(student)