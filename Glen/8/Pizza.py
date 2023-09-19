def make_pizza(size,*toppings):
    print("\nMaking a "+ str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("- ",topping)
    
def welcome():
    print("today I'll love to eat pizza")