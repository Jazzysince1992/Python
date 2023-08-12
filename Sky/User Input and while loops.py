# 7-1
# carType = input("Please enter the car you want to rent: ")
# print("Let me see if I can find you a "+carType)
#7-2
# noOfPeople = input("How many number of people are in their dinner group: ")
# if int(noOfPeople)>8:
#     print("They will have to wait for a table")
# else:
#     print("Table is ready")
# 7-3

# while True:
#     topping = input("Please enter the topping: ")
#     if topping.lower() =="quit":
#         break
#     print("Adding",topping,"to your pizza.")
#     listOfTopping.append(topping)

#7-5
# while True:
#     age = input("Please enter your age: ")
#     if int(age)<=3:
#         print("The ticket is free")
#     elif int(age)>3 and int(age)<=12:
#         print("The ticket is $10")
#     elif int(age)>12:
#         print("The ticket is $15")

# # 7-6
# topping = ''
# while topping.lower()!= 'quit':
#     topping = input("Enter a pizza topping (or 'quit' to exit): ")
#     if topping.lower!= 'quit':
#         print("Adding ",topping," to your pizza")

# active = True
# while active:
#     topping = input("Enter a pizza topping (or 'quit' to exit): ")
#     if topping.lower()=='quit':
#         active=False
#     else:
#         print("Adding ",topping," to your pizza")

# while True:
#     topping = input("Enter a pizza topping (or 'quit' to exit): ")
#     if topping.lower()=='quit':
#         break
#     print("Adding ",topping," to your pizza")

# i=1
# while i>0:
#     print(i)
#     i+=1
#     print(i)

# sandwich_orders = ["tuna", "ham and cheese", "turkey club", "veggie", "BLT"]
# finished_sandwiches = []

# while sandwich_orders:
#     current_order = sandwich_orders.pop(0)
#     print("I made your", current_order, "sandwich.")
#     finished_sandwiches.append(current_order)

# print("\nList of finished sandwiches:")
# for sandwich in finished_sandwiches:
#     print(sandwich)
# print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
# sandwich_orders = ["tuna", "ham and cheese", "turkey club","pastrami", "veggie" ,"pastrami","BLT","pastrami"]
# finished_sandwiches = []
# print(sandwich_orders)
# print("Sorry, the deli has run out of pastrami")

# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# print(sandwich_orders)
# while sandwich_orders:
#     current_order = sandwich_orders.pop(0)
#     print("I made your", current_order, "sandwich.")
#     finished_sandwiches.append(current_order)

# print("\nList of finished sandwiches:")
# for sandwich in finished_sandwiches:
#     print(sandwich)

destinationList = []
while True:
    destination = input("Please enter your dream vacation: ")
    destinationList.append(destination)
    if destination== 'quit':
        break

for destination in destinationList:
    print(destination)

