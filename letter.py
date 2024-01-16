def letterHistogram(letters):
    
    histogram = {};

    for letter in letters:
        if letter.isalpha():
            if letter in histogram:
                histogram[letter] += 1;
            else: 
                histogram[letter] = 1;

    return histogram;    



userInput = input("type some letters: ");

result = letterHistogram(userInput);
print(result);
