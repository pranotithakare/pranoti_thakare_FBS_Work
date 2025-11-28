###3. Python Program to Check if a Given Key Exists in a Dictionary or Not.
def key_exists(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False
my_dict = {'name': 'mau', 'age': 22, 'city': 'Satana'}

key_to_check = 'age'

if key_exists(my_dict, key_to_check):
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does NOT exist in the dictionary.")
