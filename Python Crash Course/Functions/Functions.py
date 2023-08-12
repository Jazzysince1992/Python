# #8.1
# def displayMesage():
#     print("I'm learning functions chapter number 7 from the book crach course python")
# displayMesage()

# #8.2
# def favBook(book):
#     print("one of my favorite book is " + book)
# favBook("Alice in wonderland")

# #8.3 & 8.4
# def makeShirt(size,message="I love Python"):
#     print("Size of the shirt is: "+str(size)+".\n And message on the shirt should be:" + message)

# makeShirt(24,"Hey Jazzy")
# makeShirt(size=45,message="How are you?")
# makeShirt(24)

#8.5
# def describeCity(city,country="Thailand"):
#     print(city+" is in "+country)

# describeCity(city="Ayutthaya")
# describeCity(city="Bangkok")
# describeCity(city="Lucknow",country="India")

# 8.6
# def cityCountry(city,country):
#     return city+" is in "+country
# message = cityCountry("Bangkok","Thailand")
# print(message)

# 8.7 & 8.8
# def album(artist,albumName):
#     return albumName+" is created by "+artist


# while True:
#     artist = input("Please enter the artist name")
#     if artist=='q':
#         break
#     albumName = input("Please enter the album name")
#     if albumName=='q':
#         break
    
# print(album(artist,albumName))


#8.9 & 8.11
# magician = ["Jazzy","Saurabh","Prasad","Jaiswal"]
# greatMagician=[]
# def showMagician(names):
#     currentMagician=""
#     for name in  names:
#         currentMagician="Great "+name
#         greatMagician.append(currentMagician)
#     print(magician)
#     print(greatMagician)


# showMagician(magician)
#8.10
# magician = ["Jazzy","Saurabh","Prasad","Jaiswal"]
# greatMagician=[]
# def showMagician(names):

#     while names:
#         currentMagician="Great "+names.pop()
#         greatMagician.append(currentMagician)
#     print(magician)
#     print(greatMagician)
# showMagician(magician)

#8.12
# def sandwitches(*items):
#     for item in items:
#         print(item)
# sandwitches("Jazzy","Saurabh","Prasad","Jaiswal")
# print("-----------------")
# sandwitches("Jazzy","Saurabh","Prasad")

#8.13
# def buildProfile(firstN,lastN,**userInfo):
#     profile={}
#     profile["firstName"] = firstN
#     profile["lastName"] = lastN
#     for k,v in userInfo.items():
#         profile[k]=v
#     return profile

# userProfile = buildProfile("Saurabh","Prasad",location="Bangkok",field="Computer")
# print(userProfile)


#8.14

def cars(brand,model,**details):
    car={}
    car["brand"]=brand
    car["model"]=model
    for k,v in details.items():
        car[k]=v
    return car

carToPrint = cars("Honda","civic",color = "Black",transmission="AT")
print(carToPrint)