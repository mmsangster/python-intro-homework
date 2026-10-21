age = int(input("How old are you? "))

if age <= 12:
    print("You are a child.")
elif age <= 17:
    print("You are a teen.")
elif age <= 64:
    print("You are an adult.")
else:
    print("You are a senior.")