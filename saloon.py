from time import sleep
from random import shuffle
from inventory import inventory

sleep_val = 1

def saloon_loop():
    print("\nYou enter the saloon and look around. It reeks of smoke and booze.")
    while True:
        where_to_go = input("Where do you want to go?\n1: Bar\n2: Faro table\n3: Back to town square\n\nChoice: ")
        if where_to_go == '1':
            bar()
        elif where_to_go == '2':
            faro_table()
        elif where_to_go == '3':
            break
        else:
            print("Sorry, didn't catch that")

# Bar

def bar():
    print('You go up to the bartender...')
    drink = input('Bartenter - "Howdy, what can I get you? 1: Beer, 2: Whiskey, 3: Margarita.": ')
    if drink == '1':
        print('You guzzle your hipstery IPA down like a fish out of water.')
    elif drink == '2':
        print('You throw back the entire bottle of whiskey in three satisfying gulps.')
    elif drink == '3':
        print('You sip on your Margarita like the classy scoundrel you are.')
    else:
        print('You down the water quickly for maximum hydration.')

# Faro table

def faro_table():
    print("""\nYou take a seat at the faro table. It's a quiet day so it's just you and the dealer.
    \nDealer - \"Welcome! Faro is popular card game around these parts. Would you like me to explain the rules?\"""")
    hear_rules()
    play_faro()

def hear_rules():
    option = input("\n1: Sure! I'm a little rusty.\n2: No thanks, I know what I'm doing.\n\nChoice: ")
    if option == '1':
        print("""\nDealer - Splendid! Here are the rules.\n
        You may place bets on any card value for ace, 2, all the way to king
        You can place multiple bets at a time!
        For the first turn, I will burn a card from the deck and show it face up.
        Then, for every turn afterwards, I will draw two cards from the deck.
        First is the dealer card. If it has the same value as one you have money on, you lose that bet.
        Second is the player's card. If you have bet on this number, you win the bet! 
        If both cards are the same, you lose half of your bet.
        If any other card is drawn, your bet stays on the table.
        \nGot it? Great!
        """)
    elif option == '2':
        print("Dealer - Well, alrighty then!")

def play_faro():
    card_values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    deck = create_deck(card_values)
    table = dict.fromkeys(card_values, 0)
    display_table(table)

    burn_card(deck)

    # put whole game from here down in loop so you can play through game
    place_all_bets(table)
    while True: 
        display_table(table)
        [dealer, player] = deal_cards(deck)
        handle_money(dealer, player, table)
        display_table(table)

        play_again = input('1: Place another bet\n2: Let dealer deal\n3: Cash out\n\nChoice: ')
        if play_again == '1':
            place_all_bets(table)
            continue
        elif play_again == '2':
            continue
        elif play_again == '3':
            cash_out(table)
            break
        else:
            print('\nInvalid input')

    # when you get to the end of the deck, force cashout so dealer can reshuffle

    
def create_deck(card_values):
    deck = []
    for _ in range(4):
        deck.extend(card_values)
    shuffle(deck)
    return deck

def draw_card(deck):
    return deck.pop()

def burn_card(deck):
    print(f'\nBurned card: {draw_card(deck)}')

def place_bet_card(table):
    while True:
        card = input("\nWhat card would you like to bet on? Enter one of the following:\nA 2 3 4 5 6 7 8 9 10 J Q K\n\nCard: ").strip().upper()
        
        if not card in table.keys():
            print("\nWe don't have that card here, try again")
            continue
        break
    return card  

def place_bet_amount(table):
    while True:
        amount = input(f"\nHow much money do you wager? Enter a number.\n(Current net worth: {inventory['money']})\n\nAmount: ")
        
        try:
            amount_number = int(amount)
        except:
            try:
                amount_number = float(amount)
            except:
                print("\nDealer - \"Sorry, I didn't catch that.\"")
                continue
        
        if amount_number <= 0:
            print("\nDealer - \"Aren't you funny! Positive numbers only please.\"")
            continue

        if amount_number > inventory['money']:
            print("\nDealer - \"You don't have enough money for that.\"")
            continue
        break
    return amount_number

def display_table(table):
    print('\n---------- Faro Table ----------')
    print(*table.keys())
    print(*table.values())
    print('--------------------------------')
    # Format more nicely with table import

def place_bet(table):
    card = place_bet_card(table)
    amount = place_bet_amount(table)
    table[card] += amount
    inventory['money'] -= amount


# place all bets in a row, then click a key to be done with it
def place_all_bets(table):
    while inventory['money'] > 0:
        place_bet(table)
        if not inventory['money'] > 0:
            break
        another = input("\nPlace another bet?\n1: Yes\n2: No\n\nChoice: ")
        if another.strip().lower() == '1':
            continue
        elif another.strip().lower() == '2':
            break
        else:
            print("\nInvalid input")

def deal_cards(deck):
    dealer = draw_card(deck)
    player = draw_card(deck)
    print(f'\nDealer card: {dealer}\nPlayer card: {player}')

    return [dealer, player]

def handle_money(dealer, player, table):
    if dealer == player:
        table[player] = try_int(table[player] * 0.5)
        return
    
    table[dealer] = 0
    table[player] *= 2

# cash out on all values function
def cash_out(table):
    inventory['money'] += sum(table.values())
    print(f"\nYour net worth is now: {inventory['money']}")

def try_int(num):
    try:
        num = int(num)
    except:
        pass
    return num

# function to color loss red, half loss yellow, and win green with background AND text color
