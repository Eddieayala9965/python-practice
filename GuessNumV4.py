import random 
randomNum = random.randint(1,10);
maxAttempts = 5
attempts = 0

while attempts < maxAttempts:
    userInput = int(input("I am thinking of a number between 1 and 10. What is the number "));

    if randomNum != userInput:
        int(userInput);
        attempts += 1
    elif randomNum == userInput:
        print("Yes! that is correct! You win !");
        break
        
    if attempts == maxAttempts:
        print("sorry no more attempts 😞");
        break;    

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

    