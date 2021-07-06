import random
import time
roll = "yes"
while roll == "yes":
    print("rolling the dice----")
    time.sleep(1)
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("the values are : ")
    print("Dice 1 = ",dice1,"\nDice 2 = ", dice2)
    choice = input("Do you want to roll the dice again? (y/n)")
    if choice.lower == "n":
        break
    