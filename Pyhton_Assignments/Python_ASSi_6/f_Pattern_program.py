#                   1 
#                 1 2 3 
#               1 2 3 4 5
#             1 2 3 4 5 6 7
#           1 2 3 4 5 6 7 8 9 




for i in range(1, 10, 2):  # Only odd numbers: 1, 3, 5, 7, 9
    spaces = (2 * 10 - i )// 2
    print('  ' * spaces, end = '')
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
