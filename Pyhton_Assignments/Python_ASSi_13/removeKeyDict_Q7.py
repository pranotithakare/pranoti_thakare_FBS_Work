###7. Python Program to Remove the Given Key from a Dictionary
def removeKey(dictionary, key_to_remove):
    if key_to_remove in dictionary:
        del dictionary[key_to_remove]
        return dictionary
    else:
        print(f"Key '{key_to_remove}' not found in dictionary.")
        return dictionary
dict = {'a': 10, 'b': 20, 'c': 30}
key = 'a'

updated_dict = removeKey(dict, key)
print("Updated Dictionary:", updated_dict)
