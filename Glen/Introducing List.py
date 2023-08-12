# myFriendsName = ['Glen','Jazzy','Planner','Python']
# print(myFriendsName[0])
# print(myFriendsName[1])
# print(myFriendsName[2])
# print(myFriendsName[3])

# i=0
# while i<4:
#     print("Hey "+myFriendsName[i]+" How are you?")
#     i+=1


#3.4
# guestList = ["Glen","Jazzy","Planner","The","Python","Tom","hero"]
# for guest in guestList:
#     print("Hello Khun "+guest.title()+" you are invited to dinner")

# i=0
# while i<len(guestList):
#     print("Hello Khun "+guestList[i]+" you are invited to dinner")
#     i+=1

# guestList.remove("The")
# guestList.remove("Python")
# guestList.append("Ryan")
# guestList.append("James")
# print(guestList)


# print("Sorry I can host only two people")
# i=len(guestList)
# while i>2:
#     guestList.pop()
#     i-=1
#     print(guestList)

# for person in guestList:
#     print("Dear Khun "+person.upper()+" You are still invited to dinner please come home at time")

# del guestList
# print(guestList)

#3.8
from audioop import reverse


places = ["Bangkok","Huahin","Ayutthaya","Kanchanburi","Chiang Mai"]
print("For Sorted: "+ str(sorted(places)))
print("Orignal List: "+ str(places))
sortedPlaces = sorted(places)
reversedPlaces = sortedPlaces.reverse()
print("For sorted and reverse " + str(sortedPlaces))
print("Orignal List: "+ str(places))
places.reverse()
print("Orignal List after reversing: "+ str(places))

# 3.9
guestList = ["Glen","Jazzy","Planner","The","Python","Tom","hero"]
print(len(guestList))