###9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String
def count_words_chars(s):
    char_count = 0
    for char in s:
        if char != " ":
            char_count += 1
    
    word_count = len(s.split())  # Count words by splitting
    return word_count, char_count

str1 = "Hello Python World"
words, chars = count_words_chars(str1)

print("Original String:", str1)
print("Number of Words:", words)
print("Number of Characters:", chars)
