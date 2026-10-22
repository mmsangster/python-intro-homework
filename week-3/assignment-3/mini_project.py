day = input("What day of the week is it? ").lower()
time = input("Is it morning, afternoon, or evening? ").lower()

if time == "morning" and (day == "saturday" or day == "sunday"):
    print("Meet a friend for coffee.")
elif time == "afternoon" and (day == "saturday" or day == "sunday"):
    print("Go to the library or bookstore.")
elif time == "evening" and day == "saturday":
    print("Go dancing.")
elif time == "evening" and day == "sunday":
    print("Have a big family dinner.")
elif time == "morning" and (day == "monday" or day == "wednesday" or day == "friday"):
    print("Go to the office.")
elif time == "morning" and (day == "tuesday" or day == "thursday"):
    print("Prepare to telework.")
elif time == "afternoon" and (day == "monday" or day == "wednesday" or day == "friday"):
    print("Attend off-site meetings.")
elif time == "afternoon" and (day == "tuesday" or day == "thursday"):
    print("Attend virtual meetings.")
elif time == "evening" and (day == "monday" or day == "wednesday" or day == "friday"):
    print("Exercise.")
elif time == "evening" and (day == "tuesday" or day == "thursday"):
    print("Spend some time on your hobbies.")
elif time != "morning" and time != "afternoon" and time != "evening":
    print("Please enter a valid time of day: morning, afternoon, or evening.")
else:
    print("Please enter a valid day of the week: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday.")