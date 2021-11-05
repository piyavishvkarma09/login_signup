# #login_singup

import json
import os
dict={}
list=[]


user=input("login or singup:")
if user=="singup":
    user_name=input("enter user name:")
    paswrd=input("enter your password:")
    if len(paswrd)>=6 and "@" in paswrd or "#" in paswrd : 
        paswrd2=input("confirm your password:")
        if paswrd==paswrd2:
            print("your account has been created succsefully:")
            dob=input("enter your date of birth;")
            city= input("your city:")
            hobby=input("enter your hobbies :")
            list1=["user","password","dob","city","hobby"]
            list2=[user,paswrd,dob,city,hobby]
            
        else:
            print("both passwords are not same")
    else:
        print("you need a strong passwoord ")
elif user=="login":
    # a=os.path.exists()
    user=input("enter your available user name:")
    password=input("enter your password :")
    if user in dict:
        print(dict[user])
    else:
        print("user not found")








# def LoginSignup():
#     def password_val(Password):
#         len_paswrd=len(Password)
#         if len_paswrd<=6:
#            print("Password should have length minimum 6.")
#         spcl='!@#$%^&*()-+'
#         list=[0,0,0,0]
#         for i in Password:
#             if i.isdigit(): 
#                list[0]=1
#             elif i.isupper():
#                 list[1]=1
#             elif i.islower():
#                 list[2]=1
#             elif i in spcl:
#                 list[3]=1               
#         if sum(list)==4:
#             pw1=True
#         else:
#             print("Password should contain atleast one uppercase, lowercase ,one special character and one number.")
#         if pw1==True:
#             pw2=input("enter Confirm password: ")
#             if Password==pw2:
#                pw_vald=True
#                print(pw_vald)
#                return pw_vald
#             else:
#                 print("Both password are not same,Try again")
#                 LoginSignup()


