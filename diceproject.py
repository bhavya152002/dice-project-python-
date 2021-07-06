# simple dice
import random
def rolldice(min, max):
    while True:
        print("rolling dice------")
        number = random.randint(min, max)
        print(f"your number : {number}")
        choice = input("Do you want to roll the dice again? (y/n)")
        if choice.lower() == 'n':
            break
rolldice(1, 6)  