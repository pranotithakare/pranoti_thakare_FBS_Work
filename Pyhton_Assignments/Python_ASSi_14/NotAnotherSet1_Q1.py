###1. Write a Python program to find elements in a given set that are not in another set.
def find_difference(set1, set2):
    return set1.difference(set2)
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7}

res = find_difference(setA, setB)
print("Elements in Set A but not in Set B:", res)
