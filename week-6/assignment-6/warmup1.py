
# Write a function that prints a greeting.
def greet(name, greeting = "Hello"):
    """Print a greeting to the user."""
    print(f"{greeting.capitalize()}, {name.capitalize()}!")

# Call the function with only a name argument.
greet("patty")

# Call the function with both a name and a custom greeting.
greet("farah", "welcome")

# Call the function with the greeting passed as a keyword argument.
greet(name = "shawty", greeting = "yo")
