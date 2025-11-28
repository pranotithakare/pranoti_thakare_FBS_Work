###6. Python Program to Find the Union of two Lists
def unionList(list1, list2):
    l = list1.copy()  
    for item in list2:
        if item not in l:  
            l.append(item)
    return l 
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
print("Union of two lists:", unionList(list1, list2))
