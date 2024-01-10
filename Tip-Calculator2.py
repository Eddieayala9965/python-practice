userTotalBill = float(input("total bill? "));
userService = input("rate your service: ");
userSplitBill = int(input("how many ways do you want to split it "));

def tipCalculate(): pass
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


if userSplitBill == 1:
    tipCalculate;
elif userSplitBill == 2:
    print("Amount per person %.2f " % int(calculateTip / 2));
elif userSplitBill == 3:
     print("Amount per person %.2f " % int(calculateTip / 3));
elif userSplitBill == 4:
     print("Amount per person %.2f " % int(calculateTip / 4));
elif userSplitBill == 5:
     print("Amount per person %.2f " % int(calculateTip / 5));
else: 
    print("invalid entry");     


