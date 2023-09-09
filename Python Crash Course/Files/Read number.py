import json
with open("Python Crash Course/Files/Your fav numbers.txt","r") as file:
    content = json.load(file)
    print(content)