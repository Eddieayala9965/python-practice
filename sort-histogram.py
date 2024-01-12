# we need to write the function, we need to create a single parameter, we need to create a var for out parameter called  "words" then we assign it sentnce.lower().split(). this will
# help check for any spelling errors, and split will split i based on white space so leaving it lank will help it dplit up the words
# then we initalize by creating a dictionary that is empty 
# from there we jump into a loop and iterate over words
#  we then update word by saywing isalpa which will only check for alphabetic strings and nothing else like a  number being in a string
# we then update again saying if word in histogram (which is he dictinary that was creeated that is empty) output histogram[word] += 1 this will update any word in there
# else will be same thing equals 1 but this is just saying it will add the inital value for it
# we return it histogram because thats what we need in order to user prompt
# then we create a var for the input asking to type a sentence
# then creat another var so we can assign it to the function and we pass our argument meaning the user input var
# and finally print and call the function

def wordHistogram(sentence):
    words = sentence.lower().split()
    sortedWords = sorted(words)
    
    histogram = {};
    for word in sortedWords:
        word = word.strip(".,?!")
        if word.isalpha():
            if word in histogram:
                histogram[word] += 1;
            else:
                histogram[word] = 1;

    return histogram

userInput = input("Enter your sentence ");

result = wordHistogram(userInput);

print(result);

