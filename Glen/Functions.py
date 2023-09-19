#8.1
# def message():
#     print("I'm learning Python")
# message()
#8.2
# def favorite_book(title):
#     print("One of my favorite books is",title)
# title = input("Please enter the title of the book you like the most")
# favorite_book(title)
#8.3 and 8.4
# def make_shirt(size="L",message="I love python"):
#     print("Customer want to order shirt of size",size,"and message should be written over it is:",message)

# make_shirt("L","I love Thailand")
# make_shirt(message="I love food",size="M")
# make_shirt()
# 8.5 & 8.6
# def cities(city,country="Thailand"):
#     print(city,"is in",country+".")
# cities("Bangkok")
# cities("Delhi","India")
# cities("Huahin")
# 8.7 & 8.8
# def make_album(name,title,number=""):
#     album = {"artist name":name,"album title":title,"Number of tracks":number}
#     return album

# while True:
#     artist = input("Please enter the artist name(or exit to quit): ")
#     if artist.lower() =="exit":
#         print("Thanks a lot!")
#         break
#     else:
#         title = input("Please enter the title: ")
#         number = input("Please enter the number of tracks: ")
#         print(make_album(artist,title))
#8.9 & 8.10
# list1 = ["Glen","Jazzy","Elon","Mark"]
# final_list=[]
# def great_magicians(list_of_Magicians):
#     for magician in list_of_Magicians:
#         final_list.append("Great "+magician)
# great_magicians(list1)
# print(final_list)
# print(list1)
#8.12
# def sandwiches(*items):
#     print("Person have ordered following items for thier sandwiches")
#     for item in items:
#         print(":",item)
# sandwiches("Cheese","Chicken","Salt","Sauce")
# sandwiches("Cheese","Chicken","Salt")
# sandwiches("Cheese","Chicken")
#8.13

# def build_profile(first, last, **user_info):
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#         return profile

# jazzy = build_profile(
#     "Saurabh","Prasad",
#     location="Bangkok",
#     field="physics"
# )
# print(jazzy)

#8.14
# def build_car(brand,model,**additional_information):
#     car_profile={}
#     car_profile['Brand Name'] = brand
#     car_profile["Model Name"] = model
#     print(additional_information)
#     for key,value in additional_information.items():
#         car_profile[key] = value
#     return car_profile        
# car1= build_car(
#     "Toyota","Camry",
#     color = "Black",
#     Cruise="yes"
# )
# print(car1)
