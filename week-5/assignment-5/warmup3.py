
#Linear search for a name and return the index without using index() function

names = ["Akatosh", "Arkay", "Dibella", "Julianos", "Kynareth", "Mara", "Stendarr", "Talos", "Zenithar"]
index = -1
user_target = input("Please enter the name you'd like to find: ")
user_target = user_target.strip().capitalize()

for i in range(len(names)):
    if names[i] == user_target:
        index = i
        break

if index != -1:
    print(f"{user_target} was found at index {index}.")
else:
    print(f"{user_target} was not found in the list.")
