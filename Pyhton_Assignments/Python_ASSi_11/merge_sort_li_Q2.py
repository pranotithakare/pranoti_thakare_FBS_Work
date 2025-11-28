###2. Python Program to Merge Two Lists and Sort it.

def merge_and_sort(list1, list2):
    merged_list = list1 + list2    
    merged_list.sort()             
    return merged_list

list1 = [5, 1, 9]
list2 = [3, 7, 2]

res = merge_and_sort(list1, list2)
print("Merged and Sorted List:", res)
