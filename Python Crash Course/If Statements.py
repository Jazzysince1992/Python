#5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
#•	 Look closely at your results, and make sure you understand why each line evaluates to True or False.
#•	 Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.

# print("--------------------")
# car =input("What is the brand of your car?\t")

# bike = input("What is the brand of your bike?\t")

# print("Is car =='Honda'? I Predict True")
# print(car=="Honda")

# print("Is bike =='Yamaha'? I Predict True")
# print(bike=="Yamaha")

# print("Is car.lower()=='honda'? I predict True")
# print(car.lower()=='honda')

# print("Is bike.lower()=='yamaha'? I predict True")
# print(bike.lower()=='yamaha')

# print("Is len(bike)==6? I predict True")
# print(len(bike)==6)

# #-------------------
# print("Is car =='benz'? I Predict false")
# print(car=="Hona")

# print("Is bike =='harley'? I Predict false")
# print(bike=="Yamah")

# print("Is car.lower()=='Benz'? I predict False")
# print(car.lower()=='hnda')

# print("Is bike.lower()=='Harley'? I predict False")
# print(bike.lower()=='ymaha')

# print("Is len(bike)==6? I predict false")
# print(len(bike)==7)


#-------------------------------------------------------------------
#5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
#•	 Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
#•	 Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)




#5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
#•	 If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
#•	 If the alien’s color isn’t green, print a statement that the player just earned 10 points.
#•	 Write one version of this program that runs the if block and another that runs the else block.

# alienColor2 = input("Enter the 2nd color of alien shot dead: ").lower()
# if alienColor2 == 'green':
#     print("You just earned 5 points for shooting alien")
# elif alienColor2=='yellow':
#     print("You just earned 10 points for shooting alien")
# elif alienColor2=='red':
#     print("You just earned 15 points for shooting alien")
# else:
#     print("Enter valid color \n =======================================")

# age=float(input("Please enter your age: "))
# if age<1:
#     print("The person ia a baby")
# elif age>=2 and age<4:
#     print("the person is a toddler")
# elif age>=4 and age<13:
#     print("the person is a Kid")
# elif age>=13 and age<20:
#     print("the person is a teenager")
# elif age>=20 and age<65:
#     print("the person is a adult")
# else:
#     print("the person is a elder")


# i=1
# fruits = []
# while i<4:
#     fruit = input("Please Enter fruit number " + str(i)+": ")
#     fruits.append(fruit)
#     i +=1

# print(fruits)
# desiredFruit = input("Please enter Which fruit you want to search? \n:")
# if desiredFruit in fruits:
#     print("yeah we have fruits in stock")
# else:
#     print("Sorry we are OOS")

#5-9
# users=["admin","Jazzy","Glen","Sky"]
# if len(users)==0:
#         print("we need some users")
# for user in users:
#     if user == "admin":
#         print("Hello " + user +",would you like to see the status report")
#     else:
#         print("Hello "+ user+", thank you for logging in again")

#5-10

# currentUsers = ["Saurabh","Prasad","Jaiswal","Jazzy","Sandhu"]
# newUsers = ["Rahul","Saurabh","Pankaj","Rocky","Shivam",]

# for user in newUsers:
#     if user in currentUsers:
#         print(user+" :The person will need to enter the new user name")
#     else:
#         print(user+" :The username is available")


#5-11
numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number == 1:
        print(str(number)+"st")
    elif number ==2:
        print(str(number)+"nd")
    elif number == 3:
        print(str(number)+"rd")
    else:
        print(str(number)+"th")