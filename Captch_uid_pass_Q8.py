###8. Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the
#same. If user enters the same number then show him success message otherwise
#failed. (Something like captcha)

import random  

user_id = input("Enter User ID: ")
password = input("Enter Password: ")

if user_id == "pranu27" and password == "pranu@123":
    
    captcha = random.randint(1000, 9999)
    print(f"Captcha: {captcha}")
    
    user_input = input("Enter the above 4-digit number: ")

    if user_input == str(captcha):
        print("✅ Login successful! Captcha verified.")
    else:
        print("❌ Login failed! Wrong captcha entered.")

else:
    print("❌ Invalid User ID or Password.")
