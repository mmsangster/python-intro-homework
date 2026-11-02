students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

top_score = 0
for student in students:
    if student["score"] > top_score:
        top_score = student["score"]

top_student = ""
for student in students:
    if student["score"] == top_score:
        top_student = student["name"]

print(f"{top_student} has the top score of {top_score}.")

class_average = 0
for student in students:
    class_average += student["score"]
class_average /= len(students)

print(f"The class average is {class_average:.2f}.")

unique_subjects = set()
for student in students:
    unique_subjects.add(student["subject"])

print(f"Unique subjects: {unique_subjects}")

high_scorers = []
for student in students:
    if student["score"] > 75:
        high_scorers.append(student["name"])

print(f"High scorers: {high_scorers}")