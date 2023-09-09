while True:
        
        try:
            num1 = int(input("Please enter first number: "))
            if num1.lower=="quit":
                break
            num2 = int(input("Please enter second number: "))
            print(num1+num2)
        except ValueError:
            print("Sorry you need to enter numbers only")