"""
Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the
function, and make sure the message displays correctly.
"""
# def display_message():
#     print("I'm learning functions in python")
# display_message()

"""
Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.
"""

# def favorite_book(title):
#     print("One of my favorite books is",title)
# favorite_book("Alice in Thailand")

"""
T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
"""


# def make_shirt(size="L",message="I love python"):
#     print("Size of the shirt is:",size,"and this message need to be printed on it: ", message.upper())

# make_shirt()
# make_shirt("xl","Today is last day")

"""
Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.
"""

# def describe_city(city,country = "Unknown Country"):
#     print(city.title(),"Is in",country.title())

# describe_city("Bangkok","Thailand")
# describe_city("London","England")
# describe_city("Banana")

"""
Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value
that’s returned.
"""

# def city_country(city,country):
#     return f"{city}, {country}"


# print(city_country("Bangkok","Thailand"))
# print(city_country("Pattaya","Thailand"))


"""Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album."""

# def make_album(artist,title,tracks=0):
#     album = {'arist':artist,'title':title}
#     if tracks!=0:
#         album['tracks'] = tracks
#     return album

# album1 = make_album("JB","Boyfriend")
# album2 = make_album("Adele","21" , tracks=13)
# print(album1)
# print(album2)

"""
Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
"""

# def make_album(artist,title,tracks=None):
#     album = {'artist':artist,'title':title}
#     if tracks is not None:
#         album['tracks'] = tracks
#     return album
# while True:
#     artist = input("Enter the artist's name or quit to exit: ")
#     if artist.lower()=="quit":
#         break
#     title = input("Enter the album's title: ")
#     tracks = input("Enter the number of tracks or press enter to skip")
#     if tracks:
#         album = make_album(artist,title,int(tracks))
#     else:
#         album = make_album(artist,title)
#     print("Album information:",album)

"""
Make a list of magician names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list
"""
# m_name = ["Jazzy","Sky","Elon"]


# def show_magician(list):
#     for name in list:
#         print(name)


# show_magician(m_name)

"""
Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified.
"""

# great_m_name= []

# def make_great(magicianlist):
#     for name in magicianlist:
#         nameWithGreat = "The Great "+name.upper()
#         great_m_name.append(nameWithGreat)

# def show_Magician(magicianlist):
#     for name in magicianlist:
#         print(name)

# m_name = ["Jazzy","Sky","Elon"]
# make_great(m_name)
# show_Magician(m_name)
# show_Magician(great_m_name)

"""
Start with your work from Exercise 8-10. Call the function make_great() with a copy of the list of magician names. Because the original list will be unchanged, return the new list and store it in a separate list. Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician name."""


"""
Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich that is being ordered. Call the function three times, using a different number of arguments each time.
"""
# def make_sandwich(*items):
#     print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
#     if not items:
#         print("Please enter atleast one item to add")
#     else:
#         print("Here's your sandwich with the follwoing items:")
#         for item in items:
#             print(item)

# make_sandwich("Cheese","Chicken","Banana","Butter")
# make_sandwich("Cheese","Chicken","Banana")
# make_sandwich("Cheese","Chicken")
# make_sandwich("Cheese","Chicken","Banana","Butter","Potato")
# make_sandwich()

""" 
Start with a copy of user_profile.py from page 153. Build
a profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.
"""

def build_profile(fname,lname):
    profile = {
        'first_name': fname,
        "last_name": lname,
    }
    profile.update(additional_info)
    return profile

my_profile = build_profile(
    fname = 'John',
    lname = 'Smith',
    age = 31,
    location = "Bangkok"
)

print(my_profile)