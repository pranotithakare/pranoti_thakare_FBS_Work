###5. Python Program to Count the Number of Vowels in a String


def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
str1 = "Hello World"
vowel_count = count_vowels(str1)
print("Original String:", str1)
print("Number of vowels:", vowel_count)
