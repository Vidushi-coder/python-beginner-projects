def game():
    import random
    
    print("Welcome to the Number Guessing Game!")
    comp_num=random.randint(0,10)
    count=0
    
    while True:
        number=int(input("Guess a number between 0 to 10: "))
        difference=abs(number-comp_num)
    
        if(difference==0):
            count+=1
            if(count==1):
                print("Correct! You guessed the number in",count, "attempt.")
            else:
                print("Correct! You guessed the number in",count, "attempts.")
            break
    
        elif(difference<=2):
            count+=1
            print("Very close! Try again")
    
        elif(number>comp_num):
            count+=1
            print("Too high! Try again")
    
        elif(number<comp_num):
            count+=1
            print("Too Low! Try again")
            
        else:
            count+=1
            print("Number is out of the given range")

game()

while True:
    play_again = input("\nDo you want to play again? (yes/no): ")
    if(play_again.lower()=="yes"):
        game()
    else:
        print("Thanks for playing! Hope you had fun")
        break