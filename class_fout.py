
# # dictionary
# from random import choice
# from unicodedata import name


# my_dict = {"key":"this is the value", "key2": "this i another key "}



# # thisis an empty dictionary
# # my_dict = dict()


# # to add  a new keu to existing keys
# # my_dict["new key"] = "this is the new value"


# # my_dict[3] = "this is the new value"





# # to create numerous bew keys 



# a = {"key7": "this is something new again", "key5": "heres another one"}


# my_dict.update(a)


# popped = my_dict.pop("key7")
# print(popped)
# print(my_dict)

# # when you pop a dict it gives you the value.

# # to find the value 

# print(my_dict["key2"])


# # to find a key that youre not sure exists

# print(my_dict.get("key7"))



    


# what extend dies to a list, update does to a dictionary



# to check the keys you have 

# print(my_dict.keys())
# #  to check all the values you have
# print(my_dict.values())


#  to see all the keys and vaues togeter but not as a dictionary 


# print(my_dict.items())
# # it creates a list if tuples. you can convert a list of tuples to a dictionary.



# b = [ ('key', 'thi sis the value'), ('key2', 'this is something'), ('key3', 'stuff i guess')]
# # breaks the lsit of tuples into a dictionary

# print(dict(b))



# to create a custom meaagse 
# to pass a defauld instead of noe
# print(my_dict.get("xyx", "not found"))


# # to change the key and assign to a new key 

# data = {"name":"chucks", "location":"aba", "job": "senior frontend", "salary": "$50,000"}

# data["city"] = data.pop("location")

# print(data)






# /////////////////////////////////////////////////////////////////////////////
# conditionals 

# if and else 

# chain conditionals elif , elif, elif , else 



# if "ada" == "john":
#     print("correct")
# else:
#         print("incorrect")


# #  class work 


# user_data = {"tolanibadmus@gmail.com": "tolani"}

# user_email =  input("enter your email: \n>").lower() 

# # use the membership operator to check if it is a key in your dictionary


# if user_email.isspace() or user_email == "":
#      print("input email")
# else:
#         if user_email in user_data.keys():
#             print("account already exists")
#         else:
#             choice = input("do you want to subscribe? (Y/y or N/n) \n>").lower()

#             # nested if is an if statement in an if statement
#             if choice == 'y':
#                 name = input("enter your full name ")
#                 user_data[user_email] = name 
#                 print("successfully subscribed")

#             elif choice == 'n':
#                 print("goodbye")

#             else:
#                 print("invalid input")

#         print(user_data)



#  membership operator is trying ti check

#  regular expressions .. popular emails in a list .. then split the email given to you by fullstop  eg .com .. then assign what was split to a variable 

#  if a = index[-1] is in your domain else; enter a valid email.



# bank app v1

from random import choice
from re import L


data = {
   "3947758475": {
       "name": "desmond",
       "dob": "09-11-11",
       "bvn": "123456789",
       "pin": "1234",
       "bal" : 0
   }
}

print("welcome to astro bank app")
print("enter s to sign up or l to login")
choice = input(">").lower()

if choice == 'l':
    acc_num = input("enter your account number: \n>")
    pin = input("enter your account pin: \n>")

    user = data.get(acc_num)

    # the user exists
    if user and user['pin'] == pin:
        print(f"welcome {user['name']}. \n your account balance is ${user['bal']}")
    else:
        print("invalid login")


# print(acc_num, " ", pin)




#  sign up

#  with draw and deposit