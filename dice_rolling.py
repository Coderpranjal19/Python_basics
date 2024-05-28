import random

def roll_dice():

    dice_drawing = {
     1:("|   1   |",
        "|   *   |",
        "|       |",),
        
     2:("|   2   |",
        "|  * *  |",
        "|       |",),

     3:("| * 3   |",
        "|   *   |",
        "|     * |",),
        
     4:("| *   * |",
        "|   4   |",
        "| *   * |",),
        
     5:("| *   * |",
        "|   * 5 |",
        "| *   * |",),

     6:("|*  * * |",
        "|   6   |",
        "|*  * * |",),
        }

    roll = input("do you want to roll the dice? (Yes/No): ")

    while roll.lower() == "Yes".lower():
        Dice1 = random.randint(1,6)
        Dice2 = random.randint(1,6)

        print(f"Dice rolled: {Dice1} and {Dice2} ")
        print("\n".join(dice_drawing[Dice1]),'\n')
        print("\n".join(dice_drawing[Dice2]))
        
        roll = input("do you want to roll the dice again ? (Yes/No): ")


roll_dice()