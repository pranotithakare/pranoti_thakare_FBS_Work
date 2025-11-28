###4. Python Program to Find the Second Largest Number in a List Using Bubble sort
def bubbleSort(li):
    for i in range(1, len(li)):
        for j in range(0,len(li)-1):
            if(li[j] > li[j+1]):
                li[j], li[j+1] = li[j+1],li[j]
                print(li)
    return li
li = [56,45,57,67,43]
print("Original list:",li)
li = bubbleSort(li)
print("Sorted list:",li)
print("Largest number in list:",li[-2])