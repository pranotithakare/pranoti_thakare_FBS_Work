###13. Python Program to count number of digits and letters in a string.
def count_letters_digits(s):
    letter_count = 0
    digit_count = 0

    for char in s:
        if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
            letter_count += 1
        elif char >= '0' and char <= '9':
            digit_count += 1

    return letter_count, digit_count

str1 = "Python123 is fun 2025!"
letters, digits = count_letters_digits(str1)

print("Original String:", str1)
print("Number of Letters:", letters)
print("Number of Digits:", digits)
