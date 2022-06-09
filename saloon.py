from time import sleep

def bar():
    sleep(1)
    print('You go up to the bartender...')
    sleep(1)
    drink = input('Bartenter - "Howdy, what can I get you? 1: Beer, 2: Whiskey, 3: Margarita.": ')
    sleep(1)
    if drink == '1':
        print('You guzzle your hipstery IPA down like a fish out of water.')
    elif drink == '2':
        print('You throw back the entire bottle of whiskey in three satisfying gulps.')
    elif drink == '3':
        print('You sip on your Margarita like the classy scoundrel you are.')
    else:
        print('You down the water quickly for maximum hydration.')

def faro_game():
    print("You take a seat at the faro table. It's a quiet day so it's just you and the dealer")
    sleep(2)
    print("\nDealer - \"Welcome! Faro is popular game around these parts. Place your bets...\"")


def saloon_loop():
    sleep(1)
    print("\nYou enter the saloon and look around. It reeks of smoke and booze.")
    while True:
        where_to_go = input("Where do you want to go?\n1: Bar\n2: Faro table\n3: Back to town square: ")
        sleep(1)
        if where_to_go == '1':
            bar()
        elif where_to_go == '2':
            faro_game()
        elif where_to_go == '3':
            break
        else:
            print("Sorry, didn't catch that")