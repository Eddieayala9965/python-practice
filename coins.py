coin_count = 0;
while True:
    userInput = input(f"you have {coin_count} coins. Would you like more (yes/no): ".lower());

    if userInput == "yes":
        coin_count += 1;
    elif userInput == "no":
        break;
    else:
        print("invalid input");
print(f"you now have {coin_count} coins. Goodbye!");

