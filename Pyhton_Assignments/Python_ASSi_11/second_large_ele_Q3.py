###3. Python Program to Sort the List According to the Second Element in Sublist
def secondEle(sublist):
  return sublist[1]

list_of_lists = [[1, 4], [3, 1], [5, 2], [6, 0]]
list_of_lists.sort(key=secondEle)
#sorted_list = sorted(list_of_lists, key=get_second_element)
print("Sorted List (by second element):", list_of_lists)

