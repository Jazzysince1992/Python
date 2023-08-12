# x = int(5)
# y= float(3.0)
# print(x+y)

# str = "   Hello How are you?   "
# print(str[2:5])
# print(str[:5])
# print(str[2:])
# print(str[-5:-2])
# print("-------------------------------------------")
# print(str.upper())
# print(str.lower())
# print(str.isupper())
# print(str.islower())
# print(str.upper().isupper())
# print(str.lower().islower())
# print(str.strip())
# print("SKYSKYSKYSKYSKYSKYSKYSKYSKYSKYSKYSKYSKYSKY")
# str1 = " Sky is a good student. He loves coding. Jazzy teach coding."
# print(str1.lower())
# print(str1.islower())
# print(str1.upper())
# print(str1.isupper())
# print(str1.strip())
# S= "Sky"
# J="Jazzy"
# print(str1.replace(S,J))
# print(str1.split(" "))

# Formating string
# age =36
# txt = "My name is Jazzy, I'm {}"
# print(txt.format(age))

# quantity = 3
# itemNo = 567
# price = 49.95

# # I want 3 pieces of item 567 for 49.95 dollars          @13:45 
# myOrder = "I want {} pieces of item {} for {} dollars"
# print(myOrder.format(quantity,itemNo,price))

# Operators +-/*%
# x=20
# y=5
# z=3
# print(x+y)
# print(x-y)
# print(x/y)
# print(x*y)
# print(x%z)
# print("==============================================")
# x += 4
# x *= 4
# x /= 2
# x -= 3
# print(x)
# print("==============================================")
# print(x!=y)
# print(x<=y)
# print(x>=y)
# print(x==y)
# & and 
# | or

# declare a variable today's_day & today's_date 
# check what day it is and date it is? 
# if it is saturday and 22 print true

# List is a collection which is ordered and changeable. Allows duplicate members.
# thisList = ["apple" , "banana", "Cherry", "apple"]
# thisList1 = [1,2,3,4]
# print(thisList)
# print(thisList[2])
# print(len(thisList))
# print(type(thisList))
# thisList[1] = "Orange"
# print(thisList)
# print(type(thisList1))
# print(type(thisList1))
# thisList.insert(1,"Romeo")
# print(thisList)


# Today_day = "Saturday"
# Today_date = "22/07/2003"
# if  Today_day == "Saturday" and Today_date == "23/07/2003":
#     print("True")
# else:
#     print("False")

# thisList = ["apple", "banana", "cherry"]
# thisList.append("Durian")
# print(thisList)
# thisList.insert(2,"Coconut")
# print(thisList)
# thatList = ["tomoto", "lemon", "Potato"]
# thisList.extend(thatList)
# print(thisList)

# thisList.remove("banana")
# print(thisList)
# thisList.pop(2)
# print(thisList)
# del thisList[0]
# print(thisList)
# thisList.clear()
# print(thisList)
# # del thisList
# print(thisList)

# print(thatList)
# a=1
# for i in thatList:
#     print(i)
#     print(a)
#     a +=1

list1 = ["Honda", "Yamaha" , "Suzuki" , "Harley"]
b=1
for j in  range(len(list1)):
    txt = "Loop number is {}"
    print(txt.format(b))
    print(list1[j])
    b+=1

# . Write a Python program to sum all the items in a list.
list2 = [2,3,4,5,10,7,8,12,9 ]
sum = 0
for i in list2:
    sum += i
print(sum)

# Write a Python program to get the largest number from a list.
max = list2[0]
for j in list2:
    if j>max:
        max=j
print(max)