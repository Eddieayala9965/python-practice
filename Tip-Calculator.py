userTotalBill = float(input("total bill? "));
userService = input("rate your service: ");

if userService == "good":
    tip = 20.00;
    calculateTip = userTotalBill + tip;
    print("your tip amount is $%.2f" % tip);
    print("your toal amount is $%.2f" % calculateTip);
elif userService == "fair":
    tip = 15.00;
    calculateTip = userTotalBill + tip;
    print("your tip amount is $%.2f" % tip);
    print("your total amount is $%.2f" % calculateTip);        
elif userService == "bad":
    tip = 10.00;
    calculateTip = userTotalBill + tip;
    print("your tip amount is $%.2f" % tip);
    print("your total amount is $%.2f" % calculateTip);
else:
    print("invalid entry"); 
    






