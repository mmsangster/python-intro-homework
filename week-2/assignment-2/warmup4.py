date = "October 10, 2026"
time = "11:00 pm"
temperature = "75 degrees"

print(f"It is now{time} on {date} and the temperature is {temperature}.")


#  File "C:\Users\User\desktop\Code the Dream\python-intro-homework\week-2\assignment-2\warmup4.py", line 5, in <module>
#    print(f"It is now {time} on {date} and the temperature is {Temperature}.")
#                                                              ^^^^^^^^^^^
# NameError: name 'Temperature' is not defined. Did you mean: 'temperature'?

# This error was caused by typing the variable "temperature" with a capital "T" instead of a lowercase "t". The variable name is case-sensitive, so it must be spelled exactly as it was defined. To fix the error, change "Temperature" to "temperature" differently in the print statement. Variable names are case-sensitive, so "temperature" and "Temperature" are not the same thing.
# I fixed it by changing "Temperature" to "temperature" in the print statement.  