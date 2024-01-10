secretNum = 5;

while True:
    userInput = int(input("I am thinking of a number between 1 and 10. What is the number "));

    if secretNum != userInput:
        int(userInput)
    elif secretNum == userInput:
        print("Yes! that is correct! You win !");
        break


    if int(userInput) == 3:
        print("3 is too low");
    if int(userInput) == 4:
        print("4 is super close");
    if int(userInput) == 6:
        print("6 is super close");
    if int(userInput) == 8:
        print("8 is too high");            
    elif int(userInput) == 9:
        print("9 is still too high");    