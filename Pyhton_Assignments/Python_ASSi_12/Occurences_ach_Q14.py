###14. Python Program to count the occurrences of ach word in a string.
def count_word_occurrences(s):
    word_list = s.split()  # Split string into words
    word_count = {}

    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

str1 = "Object Oriented programming is a concept of python  and Python is a powerful tool"
word_freq = count_word_occurrences(str1)

print("Original String:", str1)
print("Word Occurrences:")
for word, count in word_freq.items():
    print(f"{word}: {count}")
