###2. Write a Python program to remove the intersection of a second set with a first set.
def removeIntersection(set1, set2):
    set1.difference_update(set2)
    return set1

setA = {1, 2, 3, 4, 5}
setB = {3, 4, 5, 6, 7}

res = removeIntersection(setA, setB)
print("Set A after removing intersection with Set B:", res)
