
from time import sleep
from inventory import inventory


def ask_clerk():
    while True:
        print('Can I help ya find anything?"')
        print('\n')
        print('1. "I\'m looking for a disguise."')
        print('2. "I\'ve been wanting to change up my appearance."')
        print('3. "I would like to FIGHT"')
        looking_choice = input('What are you looking for?')
        if looking_choice == '1':
            sleep(2)
            print('\n' * 20)
            print('Clerk: "I mean, if you really really want one of those, we\'ve got em. But it\'s gonna cost ya."')
            sleep(2)
            print('\nThe clerk walks to the back of the store and disappears for a minute or two...')
            sleep(5)
            print('He finally comes back with a disguise kit in his hands.')
            sleep(2)
            print('\nClerk: Here is what we have. I\'m asking a fair bit, at 300 gold. Take it or leave it.')
            print('\n')
            print(inventory['money'])
            if not inventory['money'] >= 300:
                print('You have no money! You thank the clerk for his time and walk back to the town square.')
                sleep(2)
                break
            else:
                pass





def store_loop():
    while True:
        sleep(2)
        print('\n' * 20)
        print('You walk inside of the store and take a quick look around. You are approached by the store clerk.')
        sleep(2)
        print('\n' * 20)
        print('Clerk: "Hey there mister! How ya doing this fine day?"')
        print('\n')
        print('1. "I\'m doing fine, how are you?"')
        print('2. "Good. What all do you have here?"')
        print('3. Don\'t say anything to the clerk.')
        converse_choice = input('What do you want to say?: ')
        if converse_choice == '1':
            sleep(1)
            print('\n' * 20)
            print('Clerk: "I\'m just dandy, thank you for asking!')
            ask_clerk()
            break
