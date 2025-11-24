###11. Write a program to accept an integer amount from user and tell minimumnumber of notes needed for representing that amount.
amt = int(input("Enter amount: "))

note_2000 = amt // 2000
amt = amt % 2000

note_500 = amt // 500
amt = amt % 500

note_200 = amt // 200
amt = amt % 200

note_100 = amt // 100
amt = amt % 100

note_50 = amt // 50
amt = amt % 50

note_20 = amt // 20
amt = amt % 20

note_10 = amt // 10
amt = amt % 10

note_5 = amt // 5
amt = amt % 5

note_2 = amt // 2
amt = amt % 2

note_1 = amt // 1
amt = amt % 1

print("Minimum number of notes required:")
print(f"2000 : {note_2000}")
print(f"500  : {note_500}")
print(f"200  : {note_200}")
print(f"100  : {note_100}")
print(f"50   : {note_50}")
print(f"20   : {note_20}")
print(f"10   : {note_10}")
print(f"5    : {note_5}")
print(f"2    : {note_2}")
print(f"1    : {note_1}")
