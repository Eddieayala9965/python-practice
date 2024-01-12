def wordHistogram(sentence):
    words = sentence.lower().split();

    histogram = {};

    for word in words:
        word = word.strip(",.?!");
        if word.isalpha():
            if word in histogram:
                histogram[word] += 1
            else:
                histogram[word] = 1

    return histogram;


userInput = input("type some words ");
result = wordHistogram(userInput);
print(result);
    