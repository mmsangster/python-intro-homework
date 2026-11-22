
with open('C:/Users/User/Desktop/Code the Dream/python-intro-homework/week-7/data/notes.txt', 'r') as file:
    for line_num, line in enumerate(file, start=1):
        print(f"Line {line_num}:", line.strip())