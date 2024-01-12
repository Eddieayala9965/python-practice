def sortHistogram(sentence):
    words = sentence.lower().split();
    sortedWords = sorted(words);
    histogram = {};

    for word in sortedWords:
        word = word.strip(",.?!");
        if word.isalpha():
            if word in histogram:
                histogram[word] += 1
            else:
                histogram[word] = 1

    return histogram;


userInput = input("type some words ");
result = sortHistogram(userInput);
print(result);
    