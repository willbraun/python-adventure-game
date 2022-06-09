import main

def stable_loop1():
    print("You enter the stable. You see the stable master")
    while True:

        choice = input("Would you like to 1. Speak to the stable master or 2. Steal his horse?")
        if choice == "1":
                print("You approach the stable master. He seems shocked to see you even you before you speak. You ask him about buying a horse. 'I recognize you!' he says, 'I would be hung for selling a horse to a known criminal! Now leave!'")
        if choice == "2":
                print("You approach the horse, moving as quietly as you can. As you lift yourself onto the saddle you spook the horse, causing it to buck. The noise alerts the stable master, who is ready with his six-shooter. A few quick shots and you're dead.  Game Over. \n Press 1. to start over, press 2. to exit")
                if choice == "1":
                        main()
                else:
                    exit()
        break