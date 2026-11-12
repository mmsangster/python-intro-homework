
# Write a function to convert Celsius to Fahrenheit.
def celsius_to_fahrenheit(c):
    fahrenheit = float((c * 9/5) + 32)
    return fahrenheit
    
# Write a function to convert Fahrenheit to Celsius.
def fahrenheit_to_celsius(f):
    celsius = float((f-32) * 5/9)
    return celsius

# Call each with a few test values. Print the results using f-strings, rounded to one decimal place.

test_values = [0, 25, 42, 63, 101]
for i in test_values:
    print(f"{i} degrees Celsius is {celsius_to_fahrenheit(i):.1f} degrees Fahrenheit.")
    
for i in test_values:
    print(f"{i} degrees Fahrenheit is {fahrenheit_to_celsius(i):.1f} degrees Celsius.")
