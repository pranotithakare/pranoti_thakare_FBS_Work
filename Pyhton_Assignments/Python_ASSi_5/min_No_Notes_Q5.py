####5. Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
#  (Use looping to optimize the problem) 
# Accept amount from user
amount = int(input("Enter the amount: "))
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
count = 0

print(f"\nMinimum number of notes for {amount}:")

for i in notes:
    if amount >= i:
        count = amount // i        # Number of notes of this type
        amount = amount % i        # Remaining amount
        print(f"₹{i} x {count}")
