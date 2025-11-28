###8. Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary.
def wordFreq(text):
    freq_dict = {}
    words = text.split()  # Split string into words
    
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
            
    return freq_dict

str1 = "Python is a easy to learn and it is open source language"
res = wordFreq(str1)
print("Word Frequencies:", res)
