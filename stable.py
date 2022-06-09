from time import sleep
import main

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
                print("You approach the horse, moving as quietly as you can. As you lift yourself onto the saddle you spook the horse, causing it to buck. The noise alerts the stable master, who is ready with his six-shooter. A few quick shots and you're dead.  Game Over. \nPress 1: to start over, \nPress 2: to exit  ")
                if choice == "1":
                        main()
                else:
                    exit()
        break
