# car = "Honda"
# print("is car =='Honda'? I predict true")
# print(car=="Honda")

# car = "Toyota"
# print("is car =='Toyota'? I predict true")
# print(car=="Toyota")

# car = "Subaru"
# print("is car =='Subaru'? I predict true")
# print(car=="Subaru")

# car = "Benz"
# print("is car =='Benz'? I predict true")
# print(car=="Benz")

# car = "Audi"
# print("is car =='Audi'? I predict true")
# print(car=="Audi")

# car = "Hond"
# print("is car =='Honda'? I predict false")
# print(car=="Honda")

# car = "Toyta"
# print("is car =='Toyota'? I predict false")
# print(car=="Toyota")

# car = "Suaru"
# print("is car =='Subaru'? I predict false")
# print(car=="Subaru")

# car = "Bnz"
# print("is car =='Benz'? I predict false")
# print(car=="Benz")

# car = "udi"
# print("is car =='Audi'? I predict false")
# print(car=="Audi")


# print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
# #5-2
# print("Hello"=="Hey")
# print("Hello"=="Hello")
# print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
# msg = "Hello World"
# print(msg.title() == "Hello World")
# print(msg.title() == "Hello World" and "Hello"=="Hello")
# print(msg.title() == "Hello World" and "Hello"=="Helo")
# print(msg.title() == "Hello World" or "Hello"=="Hello")
# print(msg.title() == "Hello World" or "Hello"=="Helo")
# print(msg.title() == "Hello Worl" or "Hello"=="Helo")

# l1 = ["Glen","Jazzy","pan"]
# print("Glen" in l1)
# print("Glen" not in l1)


# # 5-4
# alien_color = "green"
# if alien_color=="green":
#     print("You just earned 5 points for shooting the alien")
# else:
#     print("You just earned 10 points")

# alien_color = "yellow"
# if alien_color=="green":
#     print("You just earned 5 points for shooting the alien")
# else:
#     print("You just earned 10 points")
# print("::::::::::::::::::::::::::::::::::::::::::::::::::::::;")
# #5-5
# alien_color = "green"
# if alien_color=="green":
#     print("You just earned 5 points")
# elif alien_color=="yellow":
#     print("You just earned 10 points")
# elif alien_color=="red":
#     print("You just earned 15 points")


# alien_color = "yellow"
# if alien_color=="green":
#     print("You just earned 5 points")
# elif alien_color=="yellow":
#     print("You just earned 10 points")
# elif alien_color=="red":
#     print("You just earned 15 points")

# alien_color = "red"
# if alien_color=="green":
#     print("You just earned 5 points")
# elif alien_color=="yellow":
#     print("You just earned 10 points")
# elif alien_color=="red":
#     print("You just earned 15 points")
# print("::::::::::::::::::::::::::::::::::::::::::::::::::::::")

# age = input("Please enter your age: ")
# if int(age)<2:
#     print("The person is a baby")
# elif int(age)>=2 and int(age)<4:
#     print("The person is a toddler")
# elif int(age)>=4 and int(age)<13:
#     print("The person is a kid")
# elif int(age)>=13 and int(age)<20:
#     print("The person is a teenager")
# elif int(age)>=20 and int(age)<65:
#     print("The person is a adult")
# elif int(age)>=65:
#     print("The person is a elder")


# fav_fruits = ["Mango","Banana","Tomato"]
# fruits = input("Enter your favorite fruit: ")
# if fruits in fav_fruits:
#     print("I really like "+fruits)
# else:
#     print("Sorry we do not have " + fruits+".")


# userName = ["Timmy","admin","Jazzy","Glen","Elon","4"]


# if len(userName)==0:
#     print("We need to find some users!")
# else:
#     for person in userName:
#         if person =="admin":
#             print("Hello admin would you like to see a status report?")
#         else:
#             print("Hello "+person+",thank you for logging in again. ")

# current_user = ["Timmy","admin","Jazzy","Glen","Elon"]
# lcu = []
# for user in current_user:
#     lu=user.lower()
#     lcu.append(lu)
#     print(lcu)

# print(lcu)

# new_user = ["Musk","Mac","Glen","Planner","jazzy"]
# for user in new_user:
#     if user.lower() in lcu:
#         print("Need to enter a new username")
#     else:
#         print("User name is available")

nlist = []
for num in range(1,10):
    nlist.append(num)
print(nlist)
finalList= []

for num in nlist:
    if num%10 == 1:
        finalList.append(str(num) +"st")
    elif num%10 == 2:
        finalList.append(str(num)+"nd")
    elif num%10 == 3:
        finalList.append(str(num) +"rd")
    else:
        finalList.append(str(num)+"th")
print(finalList)

