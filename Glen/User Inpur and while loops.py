# car_model = input("What car model you want to rent? ")
# print("Let me see if I can find you a",car_model,".")

# number_of_guests = int(input("Please enter the number of people you have: "))
# print(type(number_of_guests))
# if number_of_guests>8:
#     print("You will have to wait for a table")
# else:
#     print("Your table is ready")

# number = int(input("please enter a number: "))
# if number%10 == 0:
#     print("Yes the number is multiple of 10")
# else:
#     print("No number is not multiple of 10")

# Pizza_Toppings = ("What toppings would you like to have on your pizza?\nPlease enter 'Quit' when you are finished!:")
# print("===============================================================")
# while True:
#     Toppings = input(Pizza_Toppings)

#     if Toppings == "Quit":
#         print("Thank you for ordering! Your order will be right with you!")
#         print("===============================================================")
#         break
#     else:
#         print("The topping has been added, is there anything else you'd like to add?")


# while True:
#     age= input("Please enter your age (or 'exit to quit): ")
#     if age.upper() == 'EXIT':
#         print("Thanks it was nice to meet you!")
#         break
#     else:
#         if int(age)<3:
#             print("Your ticket is free. Enjoy the movie!")
#         elif int(age)>=3 and int(age)<12:
#             print("The ticket cost $10, Enjoy the movie!")
#         else:
# #             print("The ticket costs $15, Enjoy the movie!")


# Active = True
# while Active:
#     message = input("Please let us know where you'd like to fly today, so we can book you a flight! Otherwise please type in quit to end the booking!")
#     if message.lower() == 'quit':
#         Active = False
#     else:
#         print("Sure thing! We'll book a flight for you!")
#         print("============================================")

# print("============================================")
# Interested_Model = input("Greetings! What car would you like to buy today?")
# Interested_Model += ("Otherwise please let us know if that is all, by saying Quit")
# message = ("Would you like any other models?")
# model = Interested_Model
# Active = True
# while Active:
#     model = input(message)
#     if model == 'Quit':
#         print("============================================")
#         Active=False

# while True:
#     number = input("Please enter a number")
#     print(number)
# while True:
    # print("This is a infinite loop")

# sandwich_orders = ["Tuna Sandwich","Meaty Madness Sandwich","Puking Potato Sandwich","Dino Rawr Sandwich","Nuggie Fries Sandwich","Greentree pizza Sandwich"]
# finished_sandwiches = []
# print("============================================")
# print("These are the sandwiches we have on our menu")
# for order in sandwich_orders:
#     print("I made your", order ,"sandwich.")
#     finished_sandwiches.append(order)

#     print("finished_sandwiches")
#     for sandwich in finished_sandwiches:
#         print(sandwich)
# print("============================================")

# sandwich_orders =["Tuna","Ham","Cheese","Egg","Bacon","Pastrami","Mushroom","Turkey","Chicken","Beef"]
# finished_sandwiches = []
# print("============================================")
# print("Welcome to the Deli! What would you like to eat today?\nWe're also sorry to inform you that we've ran out of Pastrami today! Once you're done please say Quit.")
# print("Here is our menu down below for you to see!")
# print(sandwich_orders)
# print("============================================")
# for order in sandwich_orders:
#     message = input("What would you to add to the order?")
#     if message == order:
#         finished_sandwiches.append(message)
#     elif message == "Pastrami":
#         print("We can not add that to the order sadly!")
#     else:
#         if message.title() == "Quit":
#             print("Thanks a lot go back to home!")
#             break
            
# print("============================================")
# print("So heres what sandwiches you've ordered!")
# print(finished_sandwiches)
# print("============================================")



# #Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times.
# sandwich_orders =["Tuna","Ham","Cheese","Egg","Bacon","Pastrami","Mushroom","Pastrami","Turkey","Pastrami"]
# finished_sandwiches=[]
# # Add code near the beginning of your program to print a message saying the deli has run out of pastrami.
# print("Deli has run out of Pastrami")
# # and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
# while "Pastrami" in sandwich_orders:
#     sandwich_orders.remove("Pastrami")
# # Make sure no pastrami sandwiches end up in finished_sandwiches.
# finished_sandwiches = sandwich_orders[:]
# print(finished_sandwiches)

poll_results = {}
active = True
print("============================================")
while active:
    name = input("What is your name? ")
    Destination = input("If you could visit one place in the world, where would you like to go? ")
    poll_results[name] = Destination
    repeat = input("Would you like to continue the poll? (yes/no) ")
    if repeat.lower() == "no":
        active = False
print("============================================")
print("Poll Results:")
for name, Destination in poll_results.items():
    print(f"{name} would like to visit {Destination}.")
print("============================================")