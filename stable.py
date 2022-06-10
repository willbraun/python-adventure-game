from time import sleep
import random

def stable_loop():
    sleep(2)
    print('\n' * 5)
    print("You enter the stable. You see the stable master working, his back is turned")
    while True:

        choice = input("Would you like to \n1: Speak to the stable master, or \n2: Steal his horse while he isn't looking?  ")
        if choice == "1":
                sleep(2)
                print('\n' * 5)
                print("You approach the stable master. He seems shocked to see you even you before you speak. You ask him about buying a horse. 'I recognize you!' he says, 'I would be hung for selling a horse to a known criminal! Now leave!' You leave  ")
        if choice == "2":
                sleep(2)
                print('\n' * 5)
                print("You approach the horse, moving as quietly as you can. As you lift yourself onto the saddle you spook the horse, causing it to buck. The noise alerts the stable master, who is ready with his six-shooter. A few quick shots and you're dead.")
                sleep(10)
                print('\n' * 2)
                print("Game Over.") 
                start_again = input("Press 1: to start over, \nPress 2: to exit  ")
                if start_again == "1":
                    break
                elif start_again == "2":
                    exit()
                else:
                    print("That's not a choice")
        

def stable_loop2():
        sleep(2)
        print('\n' * 5)
        print("You enter the stable. The stable master sees you and approaches.")
        sleep(1)
        print("Well, I've never seen you around here before.  You must be new in town. How can I help you?")
        while True:
            sleep(2)
            print("I need a ticket for the first stagecoach leaving town.")
            sleep(2)
            print("Leaving so soon? Can't say I blame you. It'll be $10")
            sleep(2)
            print("I don't have $10...")
            gamble = input("Would you like to\n 1: Gamble, or \n 2: Beg")
            if gamble == "1":
                print("Are you a gamblin' man?")
                print("Why yes I am. I gotta game we can play.")
            else:
                print("... I ... I really need this ticket. I'm not a begging man typically but today I am.  Please, find it in your heart to help me out.")
                print("'Quit yer blubberin'. What if made a wager. If you win you get yer ticket, if I win ...")
                continue

def cointoss():
    while True:
        guess = input("Press 1 for 'heads'\nPress 2 for 'tails': ")
        if(guess == "1"):
            print("\n 'I choose heads'")
        elif(guess == "2"):
            print("\n 'I choose tails.'")
        else:
            print("\n'That ain't no choice!!'")
        flip = random.choice(["1", "2"])
        
        if(flip == "1"):
                sleep(2)
                print("The coin hits the ground - on heads")
        else:
                sleep(2)
                print("The coin hits the ground - on tails")
        
        if(flip == guess):
                sleep(2)
                print("'Fine... you win, you go first.'")
        else:
                sleep(2)
                print("'Ha! Not off to a good start, are you? I'll go first.'")
