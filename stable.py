from time import sleep

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
                    print("Press 1: to start over, \nPress 2: to exit")
        

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
            choice = input("Would you like to\n 1: Beg, or \n 2: Gamble")
            if choice == "1":
                print("... I ... I really need this ticket. I'm not a begging man typically but today I am.  Please, find it in your heart to help me out.")
            else:
                print("Are you a gambling man?")