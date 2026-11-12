
# Write a function that returns True if score is an integer 0-100

def is_valid_score(score):
    if score >=0 and score <= 100:
        return True
    else:
        return False
#Use input to ask the user for a score and convert it to an integer

score = int(input("Please enter a score: "))

# Call function inside an if statement and print valid or invalid.

if is_valid_score(score):
    print("Valid score.")
else:
    print("Invalid score - must be between 0 and 100.")
