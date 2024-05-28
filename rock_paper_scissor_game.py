import random

choice = ['rock','paper','scissor']

player = None
player = input("player's choice :")
computer = random.choice(choice)
print(f"computer chocie:{computer}")
loop = 'y'
loop = loop.lower()
while loop == 'y':
    if player == computer:
        print("it's a Tie!", "Do you want to play more:(y/n)?")
        inp1 = input()
        player = input("player's choice :")
        computer = random.choice(choice)
        print(f"computer chocie:{computer}")
        if inp1 == 'y':
            loop = 'y'
        else:
            loop = 'n'

    elif player == 'rock':
        if computer == 'paper':
            print("computer wins")
            loop = 'n'
        elif computer == 'scissor':
            print("player wins")
            loop = 'n'
            

    elif player == 'paper':
        if computer == 'scissor':
            print("computer wins")
            loop = 'n'
        elif computer == 'rock':
            print("player wins")
            loop = 'n'
            
    elif player == 'scissor':
        if computer == 'rock':
            print("computer wins")
            loop = 'n'
        elif computer == 'paper':
            print("player wins")
            loop = 'n'
            
    
    else:
       if player != (choice):  
        print("Please enter valid keys!")
        player = input("player's choice :")
        computer = random.choice(choice)
        print(f"computer chocie:{computer}")
        loop = 'y'



    