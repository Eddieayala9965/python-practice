def word_histogram(sentence):
    words = sentence.lower().split
   
    histogram = {}
  
    for word in words:
        word = word.strip(".,!?")
        if word.isalpha():
            if word in histogram:
                histogram[word] += 1
            else:
                histogram[word] = 1
    
    return histogram


user_sentence = input("Please enter a sentence: ")

result_histogram = word_histogram(user_sentence)

print(result_histogram)

