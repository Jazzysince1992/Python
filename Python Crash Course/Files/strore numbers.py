import json
number = input("Please enter your favorite number: ")
with open("Python Crash Course/Files/Your fav numbers.txt","w") as file:
    json.dump(number,file)