
import os

print(os.getcwd())

if os.path.exists("c:/users/user/desktop/code the dream/python-intro-homework/week-7/data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

path = os.path.join("..", "data", "expenses.csv")
print(path)
