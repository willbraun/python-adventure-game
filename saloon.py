from time import sleep
from random import shuffle

sleep_val = 1

def saloon_loop():
    print("\nYou enter the saloon and look around. It reeks of smoke and booze.")
    while True:
        where_to_go = input("Where do you want to go?\n1: Bar\n2: Faro table\n3: Back to town square:\n\nChoice: ")
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
    option = input("\n1: Sure! I'm a little rusty.\n2: No thanks, I know what I'm doing\n\nChoice: ")
    if option == '1':
        print("""\nDealer - Splendid! Here are the rules.\n
        You may place bets on any card value for ace, 2, all the way to king
        You can place multiple bets at a time!
        For the first turn, I will burn a card from the deck and show it face up.
        Then for every turn afterwards, I will then draw two cards from the deck.
        First is the dealer card. If it has the same value as one you have money on, you lose that bet.
        Second is the player's card. If you have bet on this number, you win the bet! 
        If an unrelated card is drawn, your bet stays.
        If both cards that are drawn are the same, you lose half of your bet. 
        \nGot it? Great!
        """)
    elif option == '2':
        print("Dealer - Well, alrighty then!")

def play_faro():
    card_values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    deck = create_deck(card_values)
    table = dict.fromkeys(card_values, 0)

    burn_card(deck)

    place_bet(table)

    # Put in loop so player can make multiple bets

    # Deal dealer and player cards

    # Win, lose, or split bets

    
    
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
        amount = input("\nHow much money do you wager? Enter a number\n\nAmount: ")
        
        try:
            number = float(amount)
        except:
            print("\nDealer - \"Sorry, I didn't catch that.\"")
            continue
        
        if number <= 0:
            print("\nDealer - \"Aren't you funny! Positive numbers only please.")
            continue
        break
    return amount

def place_bet(table):
    card = place_bet_card(table)
    amount = place_bet_amount(table)
    table[card] = amount