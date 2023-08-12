# 6-1
person1 = {
    "first_name": "Saurabh",
    "last_name":"Prasad",
    "age": 31,
    "city": "Bangkok"
}
person2 = {
    "first_name": "Elon",
    "last_name":"Musk",
    "age": 48,
    "city": "London"
}

print(person1["first_name"])
print(person1["last_name"])
print(person1["age"])
print(person1["city"])
print("--------------------------------------------------")
print(person2["first_name"])
print(person2["last_name"])
print(person2["age"])
print(person2["city"])
#6-2
favorite_number = {
    "jazzy" :4,
    "sky" :5,
    "Planner" : 8
}
print(favorite_number["jazzy"])
print("--------------------------")

glossary = {
    "list":"It is used to store a lot of values at a time.",
    "python":"A programming laguages",
    "dictionary":"It is use to store key valued pairs",
    "Planner":"Place where people come to do preparation",
    "Jazzy": "teacher who teach computer, maths, physics"
}

#6-4
for words,meaning in glossary.items():
    print(words+" : "+meaning)
print("-------------------------------------------------------------")
#6-5
rivers = {
    "chaophraya" : "Thailand",
    "nile":"Egypt",
    "amazon":"Brazil",
    "ganga":"India"
}

for river,country in rivers.items():
    print("The "+river +" runs through "+country+".")
print("-------------------------------------------------------------")
for river in rivers.keys():
    print(river.title())
print("-------------------------------------------------------------")
for country in rivers.values():
    print(country.title())    

print("-------------------------------------------------------------")

#6-6

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
people_to_poll = ["jen","sky","jazzy","elon","ryan","phil","sarah"]

for person in people_to_poll:
    if person in favorite_languages:
        print("Thank you " +person+" for responding.")
    else:
        print("Hello "+person+ " We invite you to take the favorite languges poll!")
print("-------------------------------------------------------------")
person1 = {
    "first_name": "Saurabh",
    "last_name":"Prasad",
    "age": 31,
    "city": "Bangkok"
}
person2 = {
    "first_name": "Elon",
    "last_name":"Musk",
    "age": 48,
    "city": "London"
}
person3 = {
    "first_name": "Ryan",
    "last_name":"Smith",
    "age": 38,
    "city": "Ayutthaya"
}
people = [person1,person2,person3]

for person in people:
    print(person['first_name']+" "+ person["last_name"]+ " is " +str(person["age"])+ " year old and living in "+ person["city"])
print("-------------------------------------------------------------")
pipo = {"kind":"dog" , "owner":"Jazzy"}
moji = {"kind":"Cat" , "owner":"Sky"}
larry = {"kind":"rabbit" , "owner":"Elon"}
richie = {"kind":"snake" , "owner":"Tom"}

pets = [pipo,moji,larry,richie]

for pet in pets:
    
    print(" is a "+ pet["kind"] + " owned by Mr/Mrs " + pet["owner"])

print("-------------------------------------------------------------")

#6-9

favorite_places = {
    "sky": ["Chiang Mai", "Phuket","Nan"],
    "jazzy":["Nonthaburi","Bangna","Pahurat","Chiang Mai", "Phuket","Nan"],
    "elon"  : ["America","London","Brazil"]
}

for name,places in favorite_places.items():
    print(name.title()+" loves to go following places:")
    count = 1
    for place in places:
        print("\t"+str(count)+" "+ place)
        count+=1

print("-------------------------------------------------------------")
favorite_number = {
    "jazzy" :[4,5,6],
    "sky" :[5,6,7,8],
    "Planner" : [8,9,10,11,12]
}

for name,numbers in favorite_number.items():
    print(name.title()+"'s favorite numbers are as follows")
    for number in numbers:
        print("\t"+str(number))

cities  = {
    "bangkok":{
        "country":"Thailand",
        "population": 3200000,
        "fact": "City of Smile"
    },
    "london":{
        "country":"England",
        "population":25000000,
        "fact":"They have london eye"
    },
    "newyork":{
        "country":"America",
        "population":35000000,
        "fact":"They have statue of liberty"
    }
}
for city , detail in cities.items():
    print(city.title() + " is present in "+detail["country"] + ". Around "+ str(detail["population"])+" lives here."+"and fun fact about them is " +detail["fact"])