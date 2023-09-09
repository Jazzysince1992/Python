try:
    print("We have following cats:")
    with open("Python Crash Course/Files/cats.txt","r") as catnames:
        cats = catnames.readlines()
        for cat in cats:
            print(cat)
    print("We have following dogs:")
    with open("Python Crash Course/Files/dog.txt","r") as dogsnames:
        dogs = dogsnames.readlines()
        for dog in dogs:
            print(dog)
except  FileNotFoundError:
    pass