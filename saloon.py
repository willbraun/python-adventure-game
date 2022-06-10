from time import sleep
from random import choice
from general import *

# Add description of bar and faro table for readers of file

sleep_val = 2

def saloon_loop():
    print("\nYou enter the saloon and look around. It reeks of smoke and booze.")
    while True:
        where_to_go = input("\nWhere do you want to go?\n1: 🍻 Bar 🍻\n2: 💰 Faro Table 💰\n3: Back to town square\n\nChoice: ")
        if where_to_go == '1':
            bar()
        elif where_to_go == '2':
            faro_table()
        elif where_to_go == '3':
            break
        else:
            print("Sorry, didn't catch that")

### Bar ###

def bar():
    order_drink()
    chat_with_stranger()

def order_drink():
    print('You go up to the bartender...')
    drink = input('Bartenter - "Howdy, what can I get you?\n1: Beer\n2: Whiskey\n3: Margarita\n\nChoice: ')
    if drink == '1':
        print('\nYou guzzle your hipstery IPA down like a fish out of water.')
    elif drink == '2':
        print('\nYou throw back the entire bottle of whiskey in three satisfying gulps.')
    elif drink == '3':
        print('\nYou sip on your Margarita like the classy scoundrel you are.')
    else:
        print('\nYou pass, regrettably, as you need to stay focused on ditching town.')

def chat_with_stranger():
    print("\nYou scan the bar, and spy some interesting townsfolk...")
    while True:
        chat = input("\nWho would you like to chat with?\n1: The town drunk\n2: The old sage\n3: The cloaked woman\n4: Nobody\n\nChoice: ")
        if chat == '1':
            town_drunk()
            continue
        elif chat == '2':
            old_man()
            continue
        elif chat == '3':
            cloaked_woman()
            continue
        elif chat == '4':
            break
        else:
            print("That person isn't here.")

def town_drunk():
    print("""\nTown drunk - \"Well howwwwdy-do to you! You look pretty beat up, and I know that from experience. Been kicked out of this bar many-a-time -- they only let me back in since I'm a good customer. Want to hear how I got kicked out last time?\"""")
    town_drunk_question()
    print("""
    \"So the story begins a week ago. Or was it last night? I can't remember. 

    Anyway, I order my rye and head straight to the faro table, and finish it before I sit down.

    I have this trick I'm perfecting, where I make a bet, see what cards are dealt, and if I lose the bet I distract the dealer by yelling "Oh my gosh, is that Abraham Lincoln in our saloon!?" -- and then I super-sneakily move my coins to the winning number.

    My snitch brother told on me and the dealer's henchmen had me swiftly removed. I thought they'd never let me back, but my bar tab keeps this establishment afloat so they can't get rid of me.

    Faro is a fickle game, I love it but I know I'll be broke soon. I robbed a bank when I was a young man but my funds are dwindling. 

    If only there were some way to know what cards are coming so I could make the correct bet...\"
""")

def town_drunk_question():
    town_drunk_answer = input("\n1: Sure!\n2: Not today\n\nChoice: ")
    if town_drunk_answer == '2':
        print("Town drunk - Oh sure ya do, I'll tell you anyway")
    else:
        print("Town drunk - Yippee!")

def old_man():
    print("""\nOld man - 
    \"Say, you must be new in town. I've seen just about everyone west of the Mississippi pass through this here saloon, I reckon.
    
    I see you eyeing that faro table. I used to be a decent player myself, but I'm not as sharp as I once was. 
    
    There's skill to it, you know. Want to know the secret?\"
    """)
    if old_man_question():
        print(f"""\nOld man - 
    \"Excellent! Now don't go off and share this, I'm only telling you this since you look like you could use a few bucks.
    
    Faro is all about card-counting. You must keep track of what's played to predict the future.

    That cloaked woman in the corner, she's real quiet but she's the best card-counter I've ever seen.

    My name is {set_color('George', green)}, tell her I sent you. I bet she has some good tips.
    \"
    """)
    else:
        print("\nOld man - \"Well that's too bad, I thought you'd be interested.\"")

def old_man_question():
    response = True
    while True:
        old_man_answer = input("\n1: I'm dying to hear it!\n2: Psh, I've got this.\n\nChoice: ")
        if old_man_answer == '1':
            break
        elif old_man_answer == '2':
            response = False
            break
        else:
            print("\nOld man - \"I can never understand the slang of the youth... come again?\"")
    return response

def cloaked_woman():
    print('cloaked woman')
    # have woman ask who sent you, and deny you if it isn't George
    # if it is, she will share that she can train you to count cards for a fee
    # pay fee, and activate new mode in faro game where you can see the upcoming player card in a new color
    # set mode as variable in this file





### Faro table ###

def faro_table():
    print("""\nYou take a seat at the faro table. It's a quiet day so it's just you and the dealer.
    \nDealer - \"Welcome! Faro is popular card game around these parts, where countless brave souls such as yourself have won and lost fortunes. Would you like me to explain the rules?\"""")
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
    table = dict.fromkeys(card_values, 0)
    display_table(table)

    burn_card(card_values)
    place_all_bets(table)
    while True: 
        display_table(table)
        [dealer, player] = deal_cards(card_values)
        handle_money(dealer, player, table)
        display_table(table)

        if not next_round(table):
            break

def draw_card(cards):
    return choice(cards)

def burn_card(cards):
    print(f'\nBurned card: {draw_card(cards)}')

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

def place_all_bets(table):
    while inventory['money'] > 0:
        place_bet(table)
        display_table(table)
        if not inventory['money'] > 0:
            break
        another = input("\nPlace another bet?\n1: Yes\n2: No\n\nChoice: ")
        if another.strip() == '1':
            continue
        elif another.strip() == '2':
            break
        else:
            print("\nInvalid input")

def deal_cards(cards):
    dealer = draw_card(cards)
    player = draw_card(cards)
    sleep(sleep_val)
    print(f'\nDealer card: {dealer}')
    sleep(sleep_val)
    print(f'Player card: {player}')
    sleep(sleep_val)

    return [dealer, player]

def handle_money(dealer, player, table):
    if dealer == player:
        table[player] = try_int(table[player] * 0.5)
        return
    
    table[dealer] = 0
    table[player] *= 2

def try_int(num):
    try:
        num = int(num)
    except:
        pass
    return num

def cash_out(table):
    inventory['money'] += sum(table.values())
    print(f"\nYour net worth is now {inventory['money']}")

def next_round(table):
    play_on = True
    while True:
        play_again = input('1: Place another bet\n2: Let dealer deal\n3: Cash out\n\nChoice: ')
        if play_again == '1':
            place_all_bets(table)
            break
        elif play_again == '2':
            break
        elif play_again == '3':
            cash_out(table)
            play_on = False
            break
        else:
            print('\nInvalid input')
    return play_on

# function to color loss red, half loss yellow, and win green with background AND text color
