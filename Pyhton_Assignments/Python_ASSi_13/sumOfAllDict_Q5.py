###5. Python Program to Sum All the Items in a Dictionary
def sum_dict_items(dictionary):
    total = 0
    for value in dictionary.values():
        total += value
    return total
my_dict = {'a': 10, 'b': 20, 'c': 30}
res = sum_dict_items(my_dict)
print("Sum of all items in the dictionary:", res)
