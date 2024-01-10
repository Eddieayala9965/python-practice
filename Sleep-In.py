from datetime import datetime

user_input = int(input("Day (0-6) "));

if user_input >= 0 and user_input <=6:
    day_name = datetime(2022, 1, 1 + user_input).strftime("%A");
    print(day_name);

    if user_input == 5:
        print("stay in, dont go to work");
    else:
        print("go to work");    
        pass
