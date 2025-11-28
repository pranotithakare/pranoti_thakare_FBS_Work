###6. Python Program to Multiply All the Items in a Dictionary
def multidictItems(dictionary):
    result = 1
    for value in dictionary.values():
        result *= value
    return result
my_dict = {'a': 10, 'b': 20, 'c': 30}
res = multidictItems(my_dict)
print("Multiplication of all items in the dictionary:", res)
