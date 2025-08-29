###11. Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.
total = 0

# Person 1
age1 = int(input("Enter age of person 1: "))
t_a1 = int(input("Enter Ticket amount of person 1: "))
if age1 <= 12:
    amt = t_a1 * 0.7
    total += amt
    print("Child discount applied. Amount after discount:", amt)
elif age1 > 59:
    amt = t_a1 * 0.5
    total += amt
    print("Senior discount applied. Amount after discount:", amt)
else:
    total += t_a1
    print("No discount applied. Amount:", t_a1)

# Person 2
age2 = int(input("Enter age of person 2: "))
t_a2 = int(input("Enter Ticket amount of person 2: "))
if age2 <= 12:
    amt = t_a2 * 0.7
    total += amt
    print("Child discount applied. Amount after discount:", amt)
elif age2 > 59:
    amt = t_a2 * 0.5
    total += amt
    print("Senior discount applied. Amount after discount:", amt)
else:
    total += t_a2
    print("No discount applied. Amount:", t_a2)

# Person 3
age3 = int(input("Enter age of person 3: "))
t_a3 = int(input("Enter Ticket amount of person 3: "))
if age3 <= 12:
    amt = t_a3 * 0.7
    total += amt
    print("Child discount applied. Amount after discount:", amt)
elif age3 > 59:
    amt = t_a3 * 0.5
    total += amt
    print("Senior discount applied. Amount after discount:", amt)
else:
    total += t_a3
    print("No discount applied. Amount:", t_a3)

# Person 4
age4 = int(input("Enter age of person 4: "))
t_a4 = int(input("Enter Ticket amount of person 4: "))
if age4 <= 12:
    amt = t_a4 * 0.7
    total += amt
    print("Child discount applied. Amount after discount:", amt)
elif age4 > 59:
    amt = t_a4 * 0.5
    total += amt
    print("Senior discount applied. Amount after discount:", amt)
else:
    total += t_a4
    print("No discount applied. Amount:", t_a4)

# Person 5
age5 = int(input("Enter age of person 5: "))
t_a5 = int(input("Enter Ticket amount of person 5: "))
if age5 <= 12:
    amt = t_a5 * 0.7
    total += amt
    print("Child discount applied. Amount after discount:", amt)
elif age5 > 59:
    amt = t_a5 * 0.5
    total += amt
    print("Senior discount applied. Amount after discount:", amt)
else:
    total += t_a5
    print("No discount applied. Amount:", t_a5)

# Final total
print("\nTotal amount to be paid by all persons:", total)
