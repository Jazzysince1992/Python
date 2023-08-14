import random
max_number=int(input("Please enter a number below which you want to guess numbers: "))
random_number = random.randrange(max_number)
num_of_guesses=0
while True:
    num_of_guesses+=1
    guessed_number = input("Please guess the number")
    
    if guessed_number.isdigit():
        guessed_number=int(guessed_number)
        if guessed_number>random_number:
            print("\n You are above the number try guessing smaller number")
            list_of_num = []
            for number in list(range(1,guessed_number)):
                list_of_num.append(number)
            print("You need to print from the follwoing list of numbers")
            print(list_of_num)
        elif guessed_number<random_number:
            print("\n You are below the number try guessing bigger number.")
            list_of_num = []
            for number in list(range(guessed_number+1,max_number+1)):
                list_of_num.append(number)
            print("You need to enter from the following list of numbers")
            print(list_of_num)
        else:
            print("Congrats you got it")
            break
    else:
        print("Please enter a valid number")

print("You guessed in",num_of_guesses,"guesses")