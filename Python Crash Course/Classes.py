# 9.1 & 9.2

# class Restaurant():
#     def __init__(self,restaurantName,cuisineType):
#         self.restaurantName = restaurantName
#         self.cuisineType = cuisineType

#     def describeRestaurant(self):
#         print(self.restaurantName +" Is opened now please come to our restaurant we provide "+ self.cuisineType.upper()+" food.")

#     def openRestaurant(self):
#         print(self.restaurantName+" Is open now")


# rm = Restaurant("Rangmahal", "Indian")
# rm.describeRestaurant()
# rm.openRestaurant()

# cho = Restaurant("Chowpati","Indian")
# cho.describeRestaurant()
# cho.openRestaurant()

# 9.3
# class User():
#     def __init__(self,fn,ln,age,city,sex):
#         self.fn = fn
#         self.ln = ln
#         self.age = age
#         self.city = city
#         self.sex = sex
    
#     def describeUser(self):
#         print("Person's full name is : "+ self.fn +" "+self.ln+".")
#         print("Person is "+self.age+" year old.")
#         print("Person lives in " + self.city)
#         print("Person is a "+ self.sex)
    
#     def greetUser(self):
#         print("Hello how are you khun " +self.fn +" "+ self.ln )

# jazzy = User("Saurabh","Prasad","31","Bangkok","Male")
# jazzy.describeUser()
# jazzy.greetUser()

# print("-----------------------")

# glen = User("Glen","Mcluen","20","Bangkok","Male")
# glen.describeUser()
# glen.greetUser()

# 9.4
# class Restaurant():
#     def __init__(self,restaurantName,cuisineType):
#         self.restaurantName = restaurantName
#         self.cuisineType = cuisineType
#         self.numberServed = 0

#     def describeRestaurant(self):
#         print(self.restaurantName +" Is opened now please come to our restaurant we provide "+ self.cuisineType.upper()+" food.")

#     def openRestaurant(self):
#         print(self.restaurantName+" Is open now")
    
#     def numberOfCustServed(self):
#         print(str(self.numberServed)+" Number of customers have been already served")
    
#     def setNumberServed(self,num):
#         self.numberServed = num
#         print("Now new number of served Cutomers are: " + str(self.numberServed))    

#     def incrementNumberServed(self,incNum):
#         self.numberServed = self.numberServed + incNum
#         print("After increment of curtomers the are: " + str(self.numberServed))

# rm = Restaurant("Rangmahal", "Indian")
# rm.describeRestaurant()
# rm.openRestaurant()
# rm.numberServed=25
# rm.setNumberServed(23)
# rm.incrementNumberServed(5)


# cho = Restaurant("Chowpati","Indian")
# cho.describeRestaurant()
# cho.openRestaurant()
# cho.numberServed=10
# cho.setNumberServed(15)
# cho.incrementNumberServed(3)

class User():
    def __init__(self,fn,ln,age,city,sex):
        self.fn = fn
        self.ln = ln
        self.age = age
        self.city = city
        self.sex = sex
        self.loginAttempts = 0 
    def describeUser(self):
        print("Person's full name is : "+ self.fn +" "+self.ln+".")
        print("Person is "+self.age+" year old.")
        print("Person lives in " + self.city)
        print("Person is a "+ self.sex)
    
    def greetUser(self):
        print("Hello how are you khun " +self.fn +" "+ self.ln )

    def incrementLoginAttempts(self):
        self.loginAttempts= self.loginAttempts +1
        print("Now login attempts are: "+ str(self.loginAttempts))
    
    def resetLoginAttempts(self):
        self.loginAttempts=0
        print("Now login attempts are: "+ str(self.loginAttempts))



jazzy = User("Saurabh","Prasad","31","Bangkok","Male")
jazzy.describeUser()
jazzy.greetUser()
jazzy.incrementLoginAttempts()
jazzy.incrementLoginAttempts()
jazzy.incrementLoginAttempts()
jazzy.incrementLoginAttempts()
jazzy.resetLoginAttempts()
print("-----------------------")

glen = User("Glen","Mcluen","20","Bangkok","Male")
glen.describeUser()
glen.greetUser()


