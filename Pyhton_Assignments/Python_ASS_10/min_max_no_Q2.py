li = [23,45,67,65,90,43]
minimum_no = li[0]
maximum_no = li[0]
for ele in li:
    if(ele > maximum_no):
        maximum_no = ele
    elif(ele < minimum_no):
        minimum_no = ele
# else:
#      None
print("Maximum Number is:",maximum_no)
print("Minimum Number is:",minimum_no)

