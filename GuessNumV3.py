import random 
randomNum = random.randint(1,10);


while True:
    userInput = int(input("I am thinking of a number between 1 and 10. What is the number "));

    if randomNum != userInput:
        int(userInput);
    elif randomNum == userInput:
        print("Yes! that is correct! You win !");
        break
        
 