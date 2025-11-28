###5. Accept a number from user and check if this element is present in the list ornot.
#  Also tell how many times it is present in the list.
num = int(input("Enter a number:"))
li = [90,89,34,56,32,32]
count = 0
for ele in li:
    if(ele == num):
        count += 1
if(count > 0):
    print(f"{num} is present in a list.")
    print(f" it is {count}  time present in a list.")
else:
     print(f"{num} is not present in list. ")

