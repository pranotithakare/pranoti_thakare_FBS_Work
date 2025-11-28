###7. Python Program to Find the Intersection of Two Lists
def intersectionList(list1, list2):
    inter = []
    for item in list1:
        if item in list2 and item not in inter: 
            inter.append(item)
    return inter

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
result = intersectionList(list1, list2)

print("Intersection of two lists:", result)
