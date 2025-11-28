###1. Python Program to Add a Key-Value Pair to the Dictionary
def add_key_value(d, key, value):
    d[key] = value  # Adding key-value pair
    return d

my_dict = {'name': 'Pranu', 'age': 22}
print("Original Dictionary:", my_dict)

updated_dict = add_key_value(my_dict, 'city', 'Nashik')

print("Updated Dictionary:", updated_dict)
