person = {
    "first_name": "Saurabh",
    "last_name": "Prasad",
    "age": 31,
    "city":"Bangkok"
}

print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])

fav_num ={
    "Jazzy":3,
    "Glen":7,
    "Elon":9,
    "Musk":8
}

for k,v in fav_num.items():
    print(k+" "+str(v))

glossary ={
    "python":"programming Language",
    "variable":"use it to store values",
    "for":"for repeating any task",
    "ifelse statement":"it is used for conditional functioning"
}

for term,meaning in glossary.items():
    print(term.upper(),": Means this: ",meaning)

river_with_country = {
    'Nile':'Egypt',
    'Chaophraya':'Thailand',
    'Thames':'England',
    'Ganga':'India'
}
for river,country in river_with_country.items():
    print("The",river,"runs through",country)
print("List of rivers are as follows:")
for river in river_with_country.keys():
    print(river)
print("List of countries are as follows:")
for country in river_with_country.values():
    print(country)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#6-6 page number 141.

person1 = {
    "first_name": "Saurabh",
    "last_name": "Prasad",
    "age": 31,
    "city":"Bangkok"
}

person2 = {
    "first_name": "Elon",
    "last_name": "Musk",
    "age": 45,
    "city":"Silicon Valley"
}

person3 = {
    "first_name": "Mark",
    "last_name": "Zuckerberg",
    "age": 43,
    "city":"Silicon Valley"
}

persons = [person1,person2,person3]

for person in persons:
    print(person["first_name"],person["last_name"]," is full name of the person")
    print(person["first_name"],person["last_name"], "is",str(person["age"]),"year old.")
    print("And the person lives in",person["city"])
    print("::::::::::::::::::::::::::::::::::::::::::::::::::")

for person in persons:
    print(person["first_name"],person["last_name"],"is full name of the person.","\nThis person is",person["age"],"year old","\nAnd lives in",person["city"])
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

pipo={
    "name":"pipo",
    "kind":"Dog",
    "owner":"Jazzy"
}
moji={
    "name":"moji",
    "kind":"Cat",
    "owner":"Aiw"
}
larry={
    "name":"larry",
    "kind":"Cat",
    "owner":"Jazzy"
}
pets = [pipo,moji,larry]
for pet in pets:
    print(pet["name"].title(),"is a",pet["kind"].lower(),"owned by",pet["owner"])

favorite_places = {
    "Jazzy":["Bangkok","Ayutthaya","Kanchanburi","Pattaya"],
    "Glen":["Bangkok","Chaingmai","Huahin","London"],
    "Elon":["America","Thailand","Phuket","India"],
    "Mark":["Thailand","India"]
}
print("------------------------------------------")
for person,places in favorite_places.items():
    print(person,"loves following places alot:")
    count=1
    for place in places:
        print(count,place)
        count+=1
    print("Person likes",count-1,"places")
    print("------------------------------------------")

favorite_numbers = {
    "Jazzy":[1,3,5,7,9],
    "Glen":[2,4,6,8,0],
    "Elon":[3,6,9],
    "Mark":[0,5,10,15,20]
}

for name,numbers in favorite_numbers.items():
    print(name,"likes following numbers:")
    for number in numbers:
        print("\t",number)

cities = {
    "Bangkok":{
        "Country":"Thailand",
        "Population":"3000000",
        "Fact":"City of smile"
    },
    "Delhi":{
        "Country":"India",
        "Population":"5000000",
        "Fact":"Delicious food"
    },
    "Kuala Lumpur":{
        "Country":"Malaysia",
        "Population":"1500000",
        "Fact":"It is beautiful"
    }
}

for name,details in cities.items():
    print("Information for",name,"are as follows")
    print("\t",name ,"is situated in",details["Country"])
    print("\t",details["Population"],"number of people lives in",name)
    print("\t fun fact about",name,"is:=>",details["Fact"].upper())
