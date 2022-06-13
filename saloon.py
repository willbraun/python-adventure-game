from time import sleep
from random import choice
from general import *

# The player enters the saloon, and can choose to either go to the bar or play faro
# Faro was a popular gambling game on the frontier before poker came around
# If the player goes to the bar, they must order a drink, then they have the option to chat with someone
# The town drunk tells how he got caught cheating at faro, but isn't necessary for gameplay
# The old man gives you a hint that you need to count cards to win at faro, and tells you his name which is important to know
# The cloaked woman requests the name of the person who sent you (the old man)
# You must enter the name correctly for her to help you
# If you do, she will offer to train you in counting cards for free - what a deal
# If you accept, when you go to the faro table, you will see the card that you should bet on
# This allows the player to win lots of money, which can be used to buy the disguise or the stagecoach ticket
# If the player goes to the faro table before being trained by the woman, the player can still play but they will not know which cards to bet on

sleep_val = 3

def saloon_loop():
    print("\nYou enter the saloon and look around. It reeks of smoke and booze.")
    while True:
        sleep(sleep_val)
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
    print('\nYou go up to the bartender...')
    sleep(sleep_val)
    drink = input(f'\n{set_color("Bartender", bright_green)}: "Howdy, what can I get you?\"\n1: Beer\n2: Whiskey\n3: Margarita\n\nChoice: ')
    sleep(sleep_val)
    if drink == '1':
        print('\nYou guzzle your hipstery IPA down like a fish out of water.')
    elif drink == '2':
        print('\nYou throw back the entire bottle of whiskey in three satisfying gulps.')
    elif drink == '3':
        print('\nYou sip on your Margarita like the classy scoundrel you are.')
    else:
        print('\nYou pass, regrettably, as you need to stay focused on ditching town.')

def chat_with_stranger():
    sleep(sleep_val)
    print("\nYou scan the bar, and spy some interesting townsfolk...")
    sleep(sleep_val)
    while True:
        chat = input(f"\nWho would you like to chat with?\n1: The {set_color('town drunk', bright_magenta)}\n2: The {set_color('old man', blue)}\n3: The {set_color('cloaked woman', yellow)}\n4: Nobody\n\nChoice: ")
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
    sleep(sleep_val)
    print(f"""\n{set_color("Town drunk", bright_magenta)}: \"Well howwwwdy-do to you! You look pretty beat up, and I know that from experience. Been kicked out of this bar many-a-time -- they only let me back in since I'm a good customer. Want to hear how I got kicked out last time?\"""")
    town_drunk_question()
    print(f"""
    \"So the story begins a week ago. Or was it last night? I can't remember. 

    Anyway, I order my rye and head straight to the faro table, and finish it before I sit down.

    I have this trick I'm perfecting, where I make a bet, see what cards are dealt, and if I lose the bet I distract the dealer by yelling "Oh my gosh, is that Abraham Lincoln in our saloon!?" -- and then I super-sneakily move my coins to the winning number.

    My snitch brother told on me and the {set_color("dealer's", cyan)} henchmen had me swiftly removed. I thought they may never let me back, but my bar tab keeps this establishment afloat so they can't get rid of me.

    Faro is a fickle game, I love it but I know I'll be broke soon. I robbed a bank when I was a young man but my funds are dwindling. 

    If only there were some way to know what cards are coming so I could make the correct bet...\"
""")
    sleep(15)

def town_drunk_question():
    town_drunk_answer = input("\n1: Sure!\n2: Not today\n\nChoice: ")
    sleep(sleep_val)
    if town_drunk_answer == '2':
        print(f"{set_color('Town drunk', bright_magenta)}: Oh sure ya do, I'll tell you anyway")
    else:
        print(f"{set_color('Town drunk', bright_magenta)}: Yippee!")

def old_man():
    sleep(sleep_val)
    print(f"""\n{set_color("Old man", blue)}:
    \"Say, you must be new in town. I've seen just about everyone west of the Mississippi pass through this here saloon, I reckon.
    
    I see you eyeing that faro table. I used to be a decent player myself, but I'm not as sharp as I once was. 
    
    There's skill to it, you know. Want to know the secret?\"
    """)
    sleep(10)
    if old_man_question():
        print(f"""\n{set_color("Old man", blue)}: 
    \"Excellent! Now don't go off and share this, I'm only telling you this since you look like you could use a few bucks.
    
    Faro is all about card-counting. You must keep track of what's played to predict the future.

    The {set_color("cloaked woman", yellow)} in the corner, she's real quiet but she's the best card-counter I've ever seen.

    My name is {set_color('George', green)}, tell her I sent you. I bet she has some good tips.\"
    """)
        sleep(10)
    else:
        print(f"\n{set_color('Old man', blue)}: \"Well that's too bad, I thought you'd be interested.\"")

def old_man_question():
    response = True
    while True:
        old_man_answer = input("\n1: I'm dying to hear it!\n2: Psh, I've got this.\n\nChoice: ")
        sleep(sleep_val)
        if old_man_answer == '1':
            break
        elif old_man_answer == '2':
            response = False
            break
        else:
            print(f"\n{set_color('Old man', blue)}: \"I can never understand the slang of the youth... come again?\"")
    return response

def cloaked_woman():
    sleep(sleep_val)
    print(f"""\n{set_color("Cloaked woman", yellow)}: \"...um, do I know you? I won't speak to you unless someone referred you to me. Who sent you?\"""")
    name = input("\nEnter name: ")
    sleep(sleep_val)
    if name.strip().lower() == "george":
        correct_name()
    else:
        print(f"\n{set_color('Cloaked woman', yellow)}: \"Hmm I don't know that person. I think you should leave.\" 🙂")

def correct_name():
    print(f"""\n{set_color('Cloaked woman', yellow)}:
    \"Oh, {set_color('George', blue)} sent you! Pardon me. I presume he sent you to learn how to count cards in faro. 
    
    We're old friends, he's jealous that I can still read the deck like a book.
    
    I'll train you for free, you look like you could use the help. Some say my skills are ✨magical✨...
    
    By tomorrow, I promise that you'll be able to count cards so you can predict the cards that appear, BEFORE the dealer draws them.

    What do you say?\"
    """)
    sleep(10)
    cloaked_woman_question()

def cloaked_woman_question():
    sleep(sleep_val)
    while True:
        cloaked_woman_answer = input("\n1: Count me in! \n2: No thanks, I'll try my luck.\n\nChoice: ")
        sleep(sleep_val)
        if cloaked_woman_answer == '1':
            training_session()
            break
        elif cloaked_woman_answer == '2':
            print(f"\n{set_color('Cloaked woman', yellow)}: \"Alright, your loss! The offer is open if you change your mind.\"")
            break
        else:
            print(f"\"{set_color('Cloaked woman', yellow)}: I'm sorry, come again?\"")

def training_session():
    print(f"\n{set_color('Cloaked woman', yellow)}: Great, lets begin!")
    sleep(sleep_val)
    print(f"""\nShe pulls out a deck of cards and a pencil, and grabs a napkin from the bar. You spend the rest of the night and the following day sitting at the bar in intense study, since your wallet and freedom depend on it. You feel like you can predict the future, and {set_color("you can't wait to head to the faro table...", green)}""")
    sleep(10)
    print(f"\n{set_color('Cloaked woman', yellow)}: Wait! before you go, here's a dollar. It'll be worth more to you than me.")
    sleep(sleep_val)
    
    inventory['money'] += 1
    print(f"\nYour net worth is now ${inventory['money']}")
    sleep(sleep_val)
    
    global can_count_cards
    can_count_cards = True

### Faro table ###

def faro_table():
    sleep(sleep_val)
    print(f"""\nYou take a seat at the faro table. It's a quiet day so it's just you and the dealer.
    \n{set_color('Dealer', cyan)}: \"Welcome! Faro is popular card game around these parts, where countless brave souls such as yourself have won and lost fortunes. Would you like me to explain the rules?\"""")
    hear_rules()

    if inventory['money'] > 0:
        play_faro()
    else:
        print(f"\n{set_color('Dealer', cyan)}: Sorry, it takes money to make money! Come back when you have some money to bet.")

def hear_rules():
    sleep(sleep_val)
    option = input("\n1: Sure! I'm a little rusty.\n2: No thanks, I know what I'm doing.\n\nChoice: ")
    sleep(sleep_val)
    if option == '1':
        print(f"""\n{set_color('Dealer', cyan)}: Here are the rules.\n
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
        print(f"{set_color('Dealer', cyan)}: Well, alrighty then!")

def play_faro():
    table = create_new_table()
    cards = list(table.keys())
    display_table(table)
    bet_this_round = 1

    burn_card(cards)
    while True: 
        [dealer, player] = determine_next_cards(cards)

        if bet_this_round == 1 or bet_this_round == 3:
            place_all_bets(table, dealer, player)

        deal_cards(dealer, player)
        handle_money(table, dealer, player)
        display_table(table)

        bet_this_round = next_round()
        if bet_this_round == 3:
            cash_out(table)
            table = create_new_table()
            display_table(table)
        if bet_this_round == 4:
            cash_out(table)
            leave_table()
            break

def create_new_table():
    card_values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    return dict.fromkeys(card_values, 0)

def draw_card(cards):
    return choice(cards)

def burn_card(cards):
    print(f'\nBurned card: {draw_card(cards)}')

def create_card_list(table, dealer, player):
    cards = list(table.keys())
    if can_count_cards:
        if dealer == player:
            cards[cards.index(player)] = set_color(player, yellow)
        else:
            cards[cards.index(dealer)] = set_color(dealer, red)
            cards[cards.index(player)] = set_color(player, green)
            
    return ' '.join(cards)

def place_bet_card(table, dealer, player):
    while True:
        card_list = create_card_list(table, dealer, player)

        card = input(f"\nWhat card would you like to bet on? Enter one of the following:\n{card_list}\n\nCard: ").strip().upper()
        
        if not card in table.keys():
            print(f"\n{set_color('Dealer', cyan)}: We don't have that card here, try again.")
            continue
        break
    return card  

def place_bet_amount():
    while True:
        amount = input(f"\nHow much money do you wager? Enter a number.\n(Current net worth: ${inventory['money']})\n\nAmount: ")
        
        try:
            amount_number = int(amount)
        except:
            try:
                amount_number = float(amount)
            except:
                print(f"\n{set_color('Dealer', cyan)}: \"Sorry, I didn't catch that.\"")
                continue
        
        if amount_number <= 0:
            print(f"\n{set_color('Dealer', cyan)}: \"Aren't you funny! Positive numbers only please.\"")
            continue

        if amount_number > inventory['money']:
            print(f"\n{set_color('Dealer', cyan)}: \"You don't have enough money for that.\"")
            continue
        break
    return amount_number

def determine_next_cards(cards):
    dealer = draw_card(cards)
    player = draw_card(cards)
    return [dealer, player]

def display_table(table):
    [cards, bets] = space_cards_and_bets(table)

    title = ' Faro Table '
    bottom_border = ('-'*(len(cards)))
    top_left_border = ('-'*((len(bottom_border) - len(title)) // 2))
    top_right_border = ('-'*(len(bottom_border) - len(top_left_border) - len(title)))

    print(f'\n{top_left_border}{title}{top_right_border}\n{cards}\n{bets}\n{bottom_border}')

def space_cards_and_bets(table):
    cards = [' ']
    bets = [' ']
    for key, value in table.items():
        card = str(key)
        bet = str(value) if value == 0 else '$' + str(value)

        if len(card) == len(bet):
            pass
        elif len(card) < len(bet):
            card = space_equally(card, bet)
        else:
            bet = space_equally(bet, card)

        if bet[0] == '$':
            bet = set_color(bet, green)

        cards.append(card)
        bets.append(bet)
    
    cards.append(' ')
    bets.append(' ')
    cards = ' | '.join(cards)
    bets = ' | '.join(bets)

    return [cards.strip(), bets.strip()]

def space_equally(short, long):
    while len(short) < len(long):
        short = ' ' + short
    return short

def place_bet(table, dealer, player):
    card = place_bet_card(table, dealer, player)
    amount = place_bet_amount()
    table[card] += amount
    inventory['money'] -= amount

def place_all_bets(table, dealer, player):
    if inventory['money'] == 0:
        print(f"\n{set_color('Dealer', cyan)}: All of your money is already on the table. I'll go ahead and deal.")
        return
    while inventory['money'] > 0:
        place_bet(table, dealer, player)
        display_table(table)
        if not inventory['money'] > 0:
            break
        
        if not another_bet():
            break

def another_bet():
    while True:
        another = input("\nPlace another bet?\n1: Yes\n2: No, let's play\n\nChoice: ")
        if another.strip() == '1':
            return True
        elif another.strip() == '2':
            return False
        else:
            print("\nInvalid input")

def deal_cards(dealer, player):
    sleep(sleep_val)
    print(f'\nDealer card: {dealer}')
    sleep(sleep_val)
    print(f'Player card: {player}')
    sleep(sleep_val)

def handle_money(table, dealer, player):
    if dealer == player and table[player] != 0:
        split_bet(table, player)
        return
    
    spoke = False
    if table[dealer] != 0:
        lose_bet(table, dealer)
        spoke = True

    if table[player] != 0:
        win_bet(table, player)
        spoke = True
    
    if not spoke:
        print(f"\n{set_color('Dealer', cyan)}: \"No changes for your bets this round.\"")
        sleep(sleep_val)
    
def split_bet(table, player):
    sleep(sleep_val)
    new_value = try_int(table[player] * 0.5)
    print(f"\n{set_color('Dealer', cyan)}: \"We drew the same card, so we'll split your bet. I'll take ${new_value}.\"")
    table[player] = new_value
    sleep(sleep_val)
    
def lose_bet(table, dealer):
    sleep(sleep_val)
    print(f"\n{set_color('Dealer', cyan)}: \"Thank you for your ${table[dealer]} on {dealer}.\"")
    table[dealer] = 0
    sleep(sleep_val)

def win_bet(table, player):
    sleep(sleep_val)
    print(f"\n{set_color('Dealer', cyan)}: \"You hit your bet of ${table[player]} on {player}!\"")
    table[player] *= 2
    sleep(sleep_val)

def try_int(num):
    try:
        num = int(num)
    except:
        pass
    return num

def cash_out(table):
    sleep(sleep_val)
    winnings = sum(table.values())
    print(f"\nCashed out ${winnings}")
    inventory['money'] += winnings
    print(f"Your net worth is now ${inventory['money']}")
    sleep(sleep_val)

def leave_table():
    print(f"\n{set_color('Dealer', cyan)}: Thanks for playing!")
    sleep(sleep_val)

def next_round():
    while True:
        play_again = input('\n1: Place another bet\n2: Let dealer deal\n3: Cash out and place another bet\n4: Cash out and leave\n\nChoice: ')
        try:
            return int(play_again)
        except:
            print('\nInvalid input')