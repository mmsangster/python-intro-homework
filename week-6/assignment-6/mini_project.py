
# Provided data

numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

# Find the minimum without using min()

def find_min(numbers):
    lowest = numbers[0]
    for number in numbers:
        if number < lowest:
            lowest = number
    return lowest

# Find the maximum without using max()

def find_max(numbers):
    highest = numbers[0]
    for number in numbers:
        if number > highest:
            highest = number
    return highest

# Linear search for user's target number

def search(numbers, target):
    
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

# Bubble sort of numbers list

def bubble_sort(numbers):
    sorted_numbers = numbers[:]
    
    swapped = True
    
    while swapped:
        swapped = False
        
        for i in range(len(sorted_numbers) -1):
            if sorted_numbers[i] > sorted_numbers[i + 1]:
                
                sorted_numbers[i], sorted_numbers[i + 1] = (
                    sorted_numbers[i + 1],
                    sorted_numbers[i]
                )
                
                swapped = True
                
    return sorted_numbers



# Menu and user's menu choice

def show_menu():
    print("""
    ======Number Cruncher======
    1. Find the minimum.
    2. Find the maximum.
    3. Search for a number.
    4. Sort the list.
    5. Quit
    ===========================
    """)
    
    ans=input("Please select an option (1-5): ")
    return ans

# Main

def main():
    
    while True:
        
        ans = show_menu()
        
        if ans == "1":
            result = find_min(numbers)
            print(f"\nThe minimum number is: {result}.")
            
        elif ans == "2":
            result = find_max(numbers)
            print(f"\nThe maximum number is: {result}.")
            
        elif ans == "3":
            search_num = int(input("\nWhat number do you want to find? "))
            
            index = search(numbers, search_num)
            
            if index != -1:
                print(f"\nYour number, {search_num}, was found at index {index}.")
            else:
                print(f"\nYour number, {search_num}, was not found.")
        
        elif ans == "4":
            sorted_numbers = bubble_sort(numbers)
            print(f"\nThe original list is: {numbers}.")
            print(f"\nThe sorted list is: {sorted_numbers}.")
            
        elif ans == "5":
            print("\nGoodbye! Thank you for using Number Cruncher!")
            break
        
        else:
            print("\nSorry, I don't recognize that input. Please try again.")
            
if __name__ == "__main__":
    main()
