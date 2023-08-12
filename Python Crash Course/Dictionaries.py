# yui = {
#     "firstName": "Parichat",
#     "lastName" : "Polsombat",
#     "age": "35",
#     "city": "Sisaket"
# }

# print(yui.get("firstName"))
# print(yui.get("nickName","Yui"))
# print(yui)


# print(favNumber)

# glossary = {
#     "Basic":"Printing statements",
#     "Comment":"To explain what below code is doing",
#     "Dictionary":"Key valued pair"
# }

# for k,v in glossary.items():
#     print("Meaning of " +k+" is "+v)

# rivers = {
#     "Egypt":"Nile",
#     "India":"Ganga",
#     "Thailand":"Chaophraya"
# }

# for k,v in rivers.items():
#     print(v+" is flowing in "+k)


# favLang = {
#     "Jazzy":"Python",
#     "Glen":"Java",
#     "Ritesh":"SQL",
#     "Puneet":"Angular",
#     "Wai wai":"Apex"
# }

# for k,v in favLang.items():
#     print(v+" is favorite language of " + k)

# jazzy = {
#     "firstName":"Saurabh",
#     "lastName":"Prasad",
#     "age": "30",
#     "city":"Bangkok"
# }

# sweety = {
#     "firstName":"Khushboo",
#     "lastName":"Jaiswal",
#     "age": "45",
#     "city":"Bangkok"
# }

# people = [yui,jazzy,sweety]

# for person in people:
#     print("Full name of the person is: "+person["firstName"]+ " " + person["lastName"])
#     print("Age of the person is: "+ person["age"])
#     print("City of the person is: " + person["city"])


# pipo = {
#     "type":"dog",
#     "owner":"Jazzy"
# }

# moji = {
#     "type":"cat",
#     "owner":"Jazzy"
# }

# richy ={
#     "type":"cat",
#     "owner":"Jazzy"
# }

# larry = {
#     "type":"cat",
#     "owner":"Jazzy"
# }

# pets = [pipo,moji,richy,larry]

# for pet in pets:
#     print("\n Type of pet is: " + pet["type"])
#     print("Owner of pet is: "+pet["owner"]+"\n")


favPlaces = {
    "jazzy": ["Bangkok", "Ayutthaya","Bangna"],
    "yui": ["Sisaket","Bangkok"],
    "sweety": ["Kanchanburi", "Ayodhya","Unnao"]
}

# for name,places in favPlaces.items():
#     print(name.title()+"'s favorite places are as follows:")
#     i=1
#     for place in places:
#         print('\t'+str(i)+". "+place)
#         i+=1
#     print('\n')

favNumbers={
    "Jazzy":[1,3,5,7,9],
    "Pinky":[2,4,6,8],
    "Sweety":[3,6,9],
    "Hansu":[4,6,8],
    "Yui":[5,10,15]
}

for name,numbers in favNumbers.items():
    print("Favorite numbers of "+name+" are as follows:")
    for number in numbers:
        print("\t-" +str(number))

cities= {
    "ayodhya":{
        "country":"India",
        "population":"100000",
        "Fun Fact":"Lord Rama was born there"
    },
    "bangkok":{
        "country":"Thailand",
        "population":"3000000",
        "Fun Fact":"it is city of angel"
        },
    "ayutthaya":{
        "country":"Thailand",
        "population":"10000",
        "Fun Fact":"Named on the name of ayodhya in India"
        }
}

for city,details in cities.items():
    print("This the name of city "+city.upper() +" Following are the etalis of the city: ")
    print("\t Above mentioned city is present in "+ details["country"])
    print("\t Above mentioned city population is "+ details["population"])
    print("\t Above mentioned city fun fact is "+ details["Fun Fact"]+"\n")








