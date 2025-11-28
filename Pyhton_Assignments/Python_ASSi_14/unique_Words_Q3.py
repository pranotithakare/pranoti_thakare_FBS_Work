###3. Write a Python program to find all the unique words and count the frequency of occurrence 
# from a given list of strings. Use Python set data type.

def cntUniqueWords(strings):
    words = []
    for line in strings:
        for word in line.split():
            words.append(word.lower())  # convert to lowercase to avoid case issues

    # Create a set of unique words
    unique_words = set(words)
    frequency = {}
    for word in unique_words:
        frequency[word] = words.count(word)

    return unique_words, frequency
string_list = [
    "Python is high level Programming language",
    "Python is easy to learn",
    "Sets are useful in Python"
]
unique, freq = cntUniqueWords(string_list)
print("Unique Words:", unique)
print("Frequencies:")
for word, count in freq.items():
    print(f"{word}: {count}")
