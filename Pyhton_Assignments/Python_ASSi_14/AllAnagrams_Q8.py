###8. Write a Python program to find all the anagrams and group them together from a given list of strings.
def group_anagrams(words):
    anagram_dict = {}

    for word in words:
        key = ''.join(sorted(word))  # sorted characters as key
        if key not in anagram_dict:
            anagram_dict[key] = set()
        anagram_dict[key].add(word)

    return list(anagram_dict.values())
words_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words_list)
print("Grouped Anagrams:")
for group in result:
    print(group)
