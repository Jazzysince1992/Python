# 7.1
# catType = input("What kind of rental car they would like?: ")
# print("Let me see if I can find you a " +catType)

#7.2
# prompt = "How many people are in their dinner group?: "
# numOfGuests = input(prompt)
# if int(numOfGuests)>8:
#     print("Sorry we are full. You will have to wait for a while")
# elif int(numOfGuests)<8:
#     print("Your table is ready")

#7.3
# num = input("Please enter a number: ")
# if int(num)%10 ==0:
#     print("Your entered number is divisible by 10")
# else:
#     print("Sorry your number is not divisible by 10")

#7.4
# pizzaToppings = ("\n Please enter the pizza toppings you want: ")
# pizzaToppings += ("\n Please enter QUIT if you are finished")
# toppings = []
# message = ""
# while message.lower() != "quit":
#     message = input(pizzaToppings)
#     toppings.append(message)
#     print(toppings)

#7.5
# prompt = "Please enter your age: \n"
# quitMessage = " Please enter quit if you are finished"
# i=1
# message = ""
# while message.lower() != "quit":
#     message = input(prompt)
#     if int(message)<3:
#         print("The ticket is free")
#     elif int(message)>3 and int(message)<12:
#         print("The ticket is 10$")
#     else:
#         print("The ticket is 15$")
#     print(quitMessage)
#     message = input()

#7.8
sandwitchOrders = ['pastrami','Jazzy','pastrami','Bangkok','pastrami','Ayutthaya']
print('Deli has run our of pastrami')
finishedSandwitches = []

while 'pastrami' in sandwitchOrders:
    sandwitchOrders.remove('pastrami')

while sandwitchOrders:
    currentSandwitch = sandwitchOrders.pop()
    finishedSandwitches.append(currentSandwitch)
    print("I made you "+ currentSandwitch.upper()+" sandwitch")

print(finishedSandwitches)