
# Provided data
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

# Menu

ans = True
while ans:
    print("""
    ======Number Cruncher======
    1. Find the minimum.
    2. Find the maximum.
    3. Search for a number.
    4. Sort the list.
    5. Quit
    ===========================
    """)
    
# User's menu choice

    ans=input("Please select an option (1-5): ")
    
# Find the minimum without using min()

    if ans=="1":
        lowest = numbers[0]
        for number in numbers:
            if number < lowest:
                lowest = number
        print(f"\nThe minimum is {lowest}.")

# Find the maximum without using max()

    elif ans=="2":
        highest = numbers[0]
        for number in numbers:
            if number > highest:
                highest = number
        print(f"\nThe maximum is {highest}.")
        
# Linear search for user's target number
      
    elif ans=="3":
        
        target = int(input("\nWhat number do you want to find?: "))
        
        def linear_search(numbers, target):
            for i in range(len(numbers)):
                if numbers[i] == target:
                    return i
            return -1
            
        result = linear_search(numbers, target)
 
 # Print result of linear search for user's target number
 
        if result != -1:
            print(f"\nYour number, {target}, was found at index {numbers.index(target)}.")
        else:
            print(f"\nYour number, {target}, was not found.")
 
        
# Bubble sort of sliced numbers list

    elif ans=="4":
        swapped_numbers = numbers[:]
        def bubble_sort(swapped_numbers):
            swapped = True
            while swapped:
                swapped = False
                for i in range(len(swapped_numbers) - 1):
                    if swapped_numbers[i] > swapped_numbers[i + 1]:
                        swapped_numbers[i], swapped_numbers[i + 1] = swapped_numbers[i + 1], swapped_numbers[i]
                        swapped = True
            return swapped_numbers
        print(f"\nThe sorted list of numbers is: {bubble_sort(swapped_numbers)}.")
  
# Exit

    elif ans == "5":
        print("\nGoodbye! Thank you for using Number Cruncher!")
        ans = None
 
 # Invalid menu choice
 
    else:
       print("\nSorry, I don't recognize that input. Please try again.")
