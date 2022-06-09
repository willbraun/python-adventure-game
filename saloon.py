from time import sleep

sleep_val = 1

def bar():
    sleep(sleep_val)
    print('You go up to the bartender...')
    sleep(sleep_val)
    drink = input('Bartenter - "Howdy, what can I get you? 1: Beer, 2: Whiskey, 3: Margarita.": ')
    sleep(sleep_val)
    if drink == '1':
        print('You guzzle your hipstery IPA down like a fish out of water.')
    elif drink == '2':
        print('You throw back the entire bottle of whiskey in three satisfying gulps.')
    elif drink == '3':
        print('You sip on your Margarita like the classy scoundrel you are.')
    else:
        print('You down the water quickly for maximum hydration.')

def faro_game():
    print("""\nYou take a seat at the faro table. It's a quiet day so it's just you and the dealer.
    \nDealer - \"Welcome! Faro is popular card game around these parts. Would you like me to explain the rules?\"""")
    hear_rules()

def hear_rules():
    option = input("\n1: Sure! I'm a little rusty.\n2: No thanks, I know what I'm doing\n\nChoice: ")
    if option == '1':
        print("""\nDealer - Splendid! Here are the rules.\n
        I will lay out 13 cards, each with a value 2 through ace.
        Place bets on any card. You can place multiple bets at a time!
        I will then draw two cards from the remaining deck.
        First is the dealer card. If it has the same value as one you have money on, you lose that bet.
        Second is the player's card. If you have bet on this number, you win the bet! 
        If an unrelated card is drawn, your bet stays.
        If both cards that are drawn are the same, you lose half of your bet. 
        \nGot it? Great!
        """)
    elif option == '2':
        print("Dealer - Well, alrighty then!")

def saloon_loop():
    sleep(sleep_val)
    print("\nYou enter the saloon and look around. It reeks of smoke and booze.")
    while True:
        where_to_go = input("Where do you want to go?\n1: Bar\n2: Faro table\n3: Back to town square:\n\nChoice: ")
        sleep(sleep_val)
        if where_to_go == '1':
            bar()
        elif where_to_go == '2':
            faro_game()
        elif where_to_go == '3':
            break
        else:
            print("Sorry, didn't catch that")