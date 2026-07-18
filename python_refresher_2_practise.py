my_list = [10, 20, 30, 40, 50, 60, 70]
print(f"list[2:5] : {my_list[2:5]}")

print(f"reverse list : {my_list[::-1]}")

x = 40
if (x > 50):
    print(f"x is greater than 50")
else:
    print(f"x is less than 50")

'''
Question 1 -
1. Take an integer as input from the user.
2. Calculate cube of the input.
3. If result > 50 print "Massive Number" else print "Small Number".
4. After this, print "EXECUTION COMPLETE!"
'''
num = int(input("Enter a number : "))
result = num ** 3
if(result > 50):
    print(f"Massive Number")
else:
    print(f"Small Number")    
print(f"EXECUTION COMPLETE!") 

'''
Question 2 -
1. Take a password as input from User.
2. Take another input to verify password.
3. Print "Successfully Verified!" if both passwords are same.
4. Print "Verification Failed!" otherwise.
'''

password = input("Enter the password")
ver_password = input("Re-Enter Password")
if(password == ver_password):
    print(f"Successfully Verified!")
else:
    print(f"Verification Failed!")    
print(f"Password Program COMPLETE!")  

time = int(input("Enter the time"))

if time > 9 and time <= 12:
    print("Good Morning :)")
elif time >= 12 and time <= 17:
    print("Good Afternoon :)")
elif time > 17 and time <= 20:
    print("Good Evening :)")
else:
    print("Good Night :)")
print(f"Time Program COMPLETE!")  

#pass statement
x = int(input("Enter a number"))
if (x > 50):
    pass
else:
    x = x + 50