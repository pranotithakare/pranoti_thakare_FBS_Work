# 4. Remove all of the vowels in a string (take input from user)
str1 = input("Enter a string:")
vowels = 'aeiouAEIOU'
remove_Vowels = ' '.join([char for char in str1  if char not in vowels])
print("String After removing vowels:", remove_Vowels)