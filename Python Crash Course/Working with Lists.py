# 4.2
print("--------------------")
animals = ["Dog","Cat","Cow","Rabbit"]
for animal in animals:
    print(animal+" is very good pet")
#4.3
print("--------------------")
for value in range(1,21):
    print(value)
#4.4
#  Make a list of the numbers from one to 1000, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)
print("--------------------")
# num=[]
# for value in range(1,1001):
#     num.append(value)

#List Comprehensions
# declareVariable = [operatedValue for tempValue in range(starting, ending-1)]
num = [value for value in range(1,11)]
for prtNum in num:
    print(prtNum)

# 4.5 Summing a 100: Make a list of the numbers from one to one hundred,and then use min() and max() to make sure your list actually starts at one and ends at one hundred. Also, use the sum() function to see how quickly Python can add a hundred numbers.
#output
# List starts at: 1
# List ends at: 100
# Sum of numbers in the list: 5050
print("--------------------")

numList = [value for value in range(1,101) ]
minValue = min(numList)
maxValue = max(numList)
sumOfNum = sum(numList)

print("List starts at: "+ str(minValue))
print("List ends at: "+ str(maxValue))
print(("Sum of numbers in the list: "+ str(sumOfNum)))

#4.6 Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
print("--------------------")
oddNum = [value for value in range(1,20,2)]
for num in oddNum:
    print(num)

#4.7 Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
print("--------------------")

threes = [value for value in range(3,31,3)]
for num in  threes:
    print(num)

#4.8. Cubes: A number raised to the third power is called a cube. For example,the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
print("--------------------")
cubes = [value**3 for value in range(1,11)]
for num in cubes:
    print(num)

#4.1
myPizzas = ["Chicken Trio", "Pan", "Pepperoni"]
for pizza in myPizzas:
    print("I love "+ pizza +" pizza alot.")
print("I can die for pizza")
print("--------------------")
#4.10. . My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas.Then, do the following:
friendPizzas =myPizzas[:]

#•	 Add a new pizza to the original list.
myPizzas.append("Hawaian")
#	 Add a different pizza to the list friend_pizzas.
friendPizzas.append("Crust")
#•	 Prove that you have two separate lists. Print the message, My favorite pizzas are:, and then use a for loop to print the first list. 
print("My favorite pizzas are:")
for mPizza in myPizzas:
    print(mPizza)

# Print the message,My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
print("My friend's favorite pizzas are:")
for fPizza in friendPizzas:
    print(fPizza)
print("--------------------")
#4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
menuTuple = ("pizza", "Burger", "Pasta","Salad","Soup")
#•	 Use a for loop to print each food the restaurant offers.
for food in menuTuple:
    print(food)
#•	 Try to modify one of the items, and make sure that Python rejects the change.
# menuTuple[0] = "Tea"
#•	 The restaurant changes its menu, replacing two of the items with different foods. Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
revisedMenu = list(menuTuple)
print(revisedMenu)
revisedMenu[0]="Tea"
revisedMenu[1]="Rice"
print(revisedMenu)
menuTuple=tuple(revisedMenu)
print(menuTuple)