#     1 
#    1 1
#   1 2 1
#  1 3 3 1




rows = int(input("Enter a row:"))

for i in range(rows):
    for j in range(rows + i):
        print(" ", end = ' ')
    val = 1
    for j in range(i + 1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1)
    print()
