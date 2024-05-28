import random 

animals = ["tiger","giraffe","elephant","mouse","horse","lion","rhino","fox","bear","donkey","zebra"]
hangman_graphics = ['__\n |',
                    '__\n |\n O',
                    '__\n |\n O\n |',
                    '__\n |\n O\n/|',
                    '__\n |\n O\n/|\ ',
                    '__\n |\n O\n/|\ \n/',
                    '__\n |\n O\n/|\ \n/ \ '
]
tries = len(hangman_graphics) - 1
word = random.choice(animals).lower()
current_guess = "_" * len(word)
wrong_guess = 0
used_letters = []

print("Welcome to Hangman")
print(f"Try to guess the word in {tries} chances")
while wrong_guess < tries and current_guess != word:
    print(hangman_graphics[wrong_guess])
    print("you have used the following letters:", used_letters)  
    print("So far the word is: ", current_guess)
    #used_letters.append(guess)
    guess = input("enter your guess :").lower()
    
    while guess in used_letters:
        print("You have already guessed that letter :", guess)
        guess = input("enter your guess :").lower()

    used_letters.append(guess)

    #check guess
    if guess in word:
        print("you have guessed correctly!")
        #give a new version of the word with guessed letter and dashes
        new_current_guess = ""
        for letter in range(len(word)):
            if guess == word[letter]:
                new_current_guess += guess
            else:
                new_current_guess += current_guess[letter]
        current_guess = new_current_guess

    else:
        print("Sorry that was incorrect")
        #increase the number of incorrect by 1
        wrong_guess += 1

#end the game
if wrong_guess == tries:
    print(hangman_graphics[wrong_guess])
    print("you have been Hanged!")
    print("The correct word is ",word)

else:
    print("You Won")


