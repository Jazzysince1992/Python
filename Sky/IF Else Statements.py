# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
# •	 If the alien is green, print a message that the player earned 5 points.
# •	 If the alien is yellow, print a message that the player earned 10 points.
# •	 If the alien is red, print a message that the player earned 15 points.
# •	 Write three versions of this program, making sure each message is printed
# for the appropriate color alien.

# color = input("Please enter a color of Alien you shot: ")
# if color == "green":
#     print("You earned 5 points")
# elif color == "yellow":
#     print("You earned 10 points")
# elif color == "red":
#     print("You earned 15 points")
# else:
#     print("Please enter valid color")

"""
5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
stage of life. Set a value for the variable age, and then:
•	 If the person is less than 2 years old, print a message that the person is
a baby.
•	 If the person is at least 2 years old but less than 4, print a message that
the person is a toddler.
•	 If the person is at least 4 years old but less than 13, print a message that
the person is a kid.
•	 If the person is at least 13 years old but less than 20, print a message that
the person is a teenager.
•	 If the person is at least 20 years old but less than 65, print a message that
the person is an adult.
•	 If the person is age 65 or older, print a message that the person is an
elder."""

# age = int(input("Please enter your age: "))
# if age<2:
#     print("You are a baby")
# elif age>2 and age<4:
#     print("You are a toddler")
# elif age>4 and age<13:
#     print("You are a kid")
# elif age>13 and age<20:
#     print("You are a teenager")
# elif age>20 and age<65:
#     print("You are a adult")
# elif age>65:
#     print("You are an elder")
# else: 
#     print("Please enter a valid age")

"""
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
independent if statements that check for certain fruits in your list.
•	 Make a list of your three favorite fruits and call it favorite_fruits.
•	 Write five if statements. Each should check whether a certain kind of fruit
is in your list. If the fruit is in your list, the if block should print a statement,
such as You really like bananas!
"""
# favFruits =[]
# i=1
# while i<=3:
#     loopNum = str(i)
#     fruit = input("Please enter your Fruit number " + i +": ")
#     favFruits.append(fruit)
#     i+=1
# print(favFruits)



"""
5-8. Hello Admin: Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user:
•	 If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
•	 Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.
"""
# users =[]
# numOfUsers = int(input("Please enter the number of users you want to enter: "))

# i=1
# while i <=numOfUsers:
#     numloop = str(i)
#     user = input("Please enter user number " + numloop+": ")
#     users.append(user)
#     i +=1
# print(users)

# for user in users:
#     if user == "admin":
#         print("Hello admin, would you like to see a status report")
#     else:
#         print("Hello "+ user +", thank you for logging in again")


"""
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
•	 If the list is empty, print the message We need to find some users!
•	 Remove all of the usernames from your list, and make sure the correct
message is printed.
"""
# users59 = []
# if len(users59) == 0:
#     print("We need to find some users!") 
# else:
#     length = str(len(users59))
#     print("We have " + length +" number of users")

"""
5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
•	 Make a list of five or more usernames called current_users.
•	 Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.
•	 Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
•	 Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted.
"""
# currentUsers = ["Jazzy","Sky","Saurabh","Prasad","Jhon"]
# newUsers = ["Sky", "jazzy", "The", "Planner"]

# for user in newUsers:
#     if user in currentUsers:
#         print(user +" is already taken You need to enter a new user name")
#     else:
#         print(user + " :Username is available!")

"""
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
•	 Store the numbers 1 through 9 in a list.
•	 Loop through the list.
•	 Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
7th 8th 9th", and each result should be on a separate line.
"""

numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number== 1:
        print("1st")
    elif number==2:
        print("2nd")
    elif number==3:
        print("3rd")
    else:
        print(str(number)+"th")
    