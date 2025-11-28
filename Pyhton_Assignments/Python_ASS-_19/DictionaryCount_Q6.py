# 6. Use a dictionary comprehension to count the length of each word
# in a sentence (take input from user)
# 6. Count the length of each word using dictionary comprehension

sentence = input("Enter a sentence: ")
word_lengths = {word: len(word) for word in sentence.split()}

print("Length of each word:", word_lengths)
