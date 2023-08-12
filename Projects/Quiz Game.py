print("welcome to my Quiz Game!")
playing = input("Do you want to play quiz game game me?").lower()
if playing == "yes":
    print("As you choose ",playing," let's play then.")
    score=0
    
    answer1 = input("What does CPU stands for? ").lower()
    if answer1 =="central processing unit":
        score+=1
        print("Congratulations your answer is correct and now your score is: ",str(score))
    else:
        print("Sorry your answer is wrong and your score is: ", str(score))
    
    answer2 = input("What does RAM stands for? ").lower()
    if answer2 =="random access memory":
        score+=1
        print("Congratulations your answer is correct and now your score is: ",str(score))
    else:
        print("Sorry your answer is wrong and your score is: ", str(score))
    
    answer3 = input("What does WHO stands for? ").lower()
    if answer3 =="world health organization":
        score+=1
        print("Congratulations your answer is correct and now your score is: ",str(score))
    else:
        print("Sorry your answer is wrong and your score is: ", str(score))
    
    answer4 = input("What does USA stands for? ").lower()
    if answer3 =="united state of america":
        score+=1
        print("Congratulations your answer is correct and now your score is: ",str(score))
    else:
        print("Sorry your answer is wrong and your score is: ", str(score))
    
else:
    print("As you choose", playing," I hope we can play some day.")
    quit()

