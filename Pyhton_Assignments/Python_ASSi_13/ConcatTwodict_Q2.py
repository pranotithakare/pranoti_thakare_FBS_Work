###2. Python Program to Concatenate Two Dictionaries Into One
# dict1 = {'a': 100, 'b': 200}
# dict2 = {'c': 300, 'd': 400}

# dict3 = dict1.copy()   
# dict3.update(dict2)

# print("Concatenated Dictionary:", dict3)


def concatenate_dicts(dict1, dict2):
    result = dict1.copy()   
    result.update(dict2)    
    return result


dict1 = {'id': 1, 'name': 'pranu'}
dict2 = {'age': 23, 'education': 'MCS'}

# Call the function
dict = concatenate_dicts(dict1, dict2)

# Output the result
print("Concatenated Dictionary:", dict)
