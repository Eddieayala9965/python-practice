# create the function have the function prompt the user so pass an arguemnet (the user input) we want to make a direcory that has an alphabet. for each letter we need to have it a vlue 
# for eacb letter, we want to have an updating counter for this dictionary
from collections import OrderedDict
histogram = {
    'letters': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
}
# so inatead of making two parameters. we decided we just hvae user input a parameter. we then created a varaible as a dictionary to resemble a counter start point. 
# we then loop over userinput. we say i user.isalpha() then if user is not th dict then 
userInput = input("type anything")
def letterHistogram(userInputs):
    count = {}
    
    for user in userInputs:
        if user.isalpha():
            if user not in count:
                count[user] = 1
            else:
                count[user] += 1

    return count

print(letterHistogram(userInput)) 




        