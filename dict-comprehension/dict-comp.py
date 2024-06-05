# TODO - use DC to create dict result, key is each word in sentence,
#  value is number of letters in word

sentence = input()
# split sentence into list of words
words = sentence.split()
print(words)
result = {word: len(word) for word in words}

print(result)