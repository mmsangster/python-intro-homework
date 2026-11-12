
# Define a variable inside a function.
def add_stuff(a, b):
    #total = a + b
    return a + b

# Try to access it outside the function and show the NameError
# NameError: name 'total' is not defined

# Return the value from the function and assign it to a variable in the outer scope. Print it to confirm it worked.

total = add_stuff(11, 353)
print(total)

