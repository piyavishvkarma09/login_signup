import json
import re #regex #for strong password#
print("welcome to login and sign up page")
user=input("what u want to do login or sign up:")
if user=="signup":
    user_name=input("enter the user_name :")
    password1=input("enter ur password:")
    if re.search("[A-Z]",password1) and re.search("[a-z]",password1) and re.search("[0-9]",password1) and  re.search("[#,$,%,&,@]",password1):
        password2=input("confirm ur password:")
        if password1==password2:
            print("congrates")
            description=input("enter ur descriptinon:")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
            dob=input("enter ur dob:")
            hobbies=input("enter ur hobbies:")
            gender=input("enter ur gender f/m :")
            print("congrates",user,"u r sucessfully signupped")
            user_details={"user_name":user_name,"password2":password2,"description":description,"dob":dob,"hobbies":hobbies,"gender":gender}
            with open("user.json","w")as file :
                a=json.dump(user_details, file,indent=2)
                # print(a) 
        else:
            print("Passwords didn't match.")                                                                                                                                    
    else:
        print("weak password")
elif user=="login":
    name=input("enter the usee_name:")
    password=input("enter the password:")
    with open("user.json","r")as file :
        data=json.load(file)
        if password==data["password2"]:
            print("congrates",name,"u have logged sucessfully")
            print("ur information is correct")
            print(data)
    
else:
    print("You have not signed up.Please signup before logging in.")