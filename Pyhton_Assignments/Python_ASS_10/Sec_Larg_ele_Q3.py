##3. Write a program to find the second largest element in the list.
li = [10,40,23,90,95]
largest_no = li[0]
second_large = li[0]
for ele in li:
    if(ele > largest_no):
        second_large = largest_no
        largest_no = ele
    elif(ele > second_large and ele != largest_no):
        second_large = ele
print("Second largest element in  the list is: ",second_large)
