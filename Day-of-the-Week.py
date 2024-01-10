from datetime import datetime
user_input = int(input("Day (0-6) "))

if user_input >= 0 and user_input <= 6:
    day_name = datetime(2022, 1, 1 + user_input).strftime("%A")
    print(day_name)
else:
    print("Invalid input. Please enter a number between 0 and 6.")