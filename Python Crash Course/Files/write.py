name = input("Please enter your name: ")
with open("Python Crash Course/Files/open.py",'w') as fileObject:
    fileObject.write(name)
    