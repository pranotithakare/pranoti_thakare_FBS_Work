###5. Write a Python program to find the longest common prefix of all strings. Use the Python set.
def longestCommonPre(words):
    if not words:
        return ""

    prefix = ""
    min_len = min(len(word) for word in words)

    for i in range(min_len):
        chars = set(word[i] for word in words)

        if len(chars) == 1:
            prefix += chars.pop()
        else:
            break

    return prefix
words = ["apple", "app", "application"]
result = longestCommonPre(words)
print("Longest common prefix:", result)
