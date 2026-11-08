# While loop with try/except

while True:
    try:
        user_number = int(input("Please enter a positive integer: "))
        if user_number >= 1:
            print(f"\nGot it. Your number is {user_number}.")
            break
        if user_number < 1:
            print("\nThat is not a positive integer. Please try again.")
    except:
        print("\nThat is not a positive integer. Please try again.")
