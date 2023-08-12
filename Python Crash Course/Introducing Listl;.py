names = ['Pari','Chat','Pol','Som','Bat']
print(names)

for name in names:
    print("Hey "+ name +" how are you?")

bikes = ["Harley","Triump", "Royal Enfield"]
for bike in bikes:
    print("I would love to have a "+bike)

guestList = ['Yui','Get','Aiw']
guestList[2] = 'Hello'
for guest in guestList:
    print("Hey " + guest +" I'll be happy to see you for dinner.")

newGuestLIst = ['Lelo','Kha lo', 'Pee lo']
guestList.extend(newGuestLIst)

print(guestList)

for guest in guestList:
    print("Hey "+guest +" Are you coming for dinner with me")

guestList.pop()
print(guestList)

guestList.pop()
print(guestList)

guestList.pop()
print(guestList)

guestList.pop()
print(guestList)

for guest in guestList:
    print("I'm sorry for so many confusion but only "+ guest +" are invited to my party")

places = ["Krabi","Lucknow","Leh Ladhak","Kerala"]
print(places)
print(sorted(places))
print(places)
places.sort()
print(places)
places.reverse()
print(places)
print(len(places))

print("Total Number of guestes coming to party are: " + str(len(guestList)))