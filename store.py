from time import sleep
import random
from general import *

# player enters store an is approached by the clerk.
# given three options, right now the two options that involve talking lead to the player having three options
# the player then can choose from directly asking for a disguise, which leads to requiring a hefty sum for it
# for the second option the player can beat around the bush asking for a disguise,
# which gives the clerk the impression you need some cosmetic help, leading him to take pity on you and offer the disguise kit for a discounted price
# the third option leads you to fight the clerk, an intense battle of fisticuffs!!! 💪🏼💪🏼💪🏼💪🏼
#
# if the player had decided not to talk, this enters ✨ SNEAKY TIME ✨
# the player must keep an eye on the clerk's whereabouts and make decisions based on the clerk's position
# if the clerk is busy doing something, the player has the option of pocketing an item
# if the clerk is not cleaning or busy, he is at the register or wandering about, keeping a watchful eye on you.
# you have the options of waiting a certain amount of time to see if the clerk is still at the register,
# of if the clerk has moved on to cleaning or restocking the shelves.
# you can only pick up things when the clerk is busy.
# other wise he will spot you and throw you out of the store AND remove everything you took from your pockets 🤠
sneaky = True

def get_caught():
    global sneaky
    sleep(1)
    print('\n' * 30)
    print('YOU GOT CAUGHT! The clerk kicked you out of the store')
    inventory['misc'] = []
    inventory['disguise'] = []
    sneaky = False


def fight_time():
    your_health = 30
    clerk_health = 30
    your_attacks = {'right hook': 5, 'uppercut': 7, 'yeehaw kimchi': 10}
    clerk_attacks = ['loose punch', 'elbow to the face', 'headbutt']
    def clerk_move():
        nonlocal your_health
        clerk_move = random.choice(clerk_attacks)
        if clerk_move == 'loose punch':
            your_health -= 2
            print('\n' * 30)
            print('Clerk threw a loose punch!')
            
        if clerk_move == 'elbow to the face':
            your_health -= 7
            print('\n' * 30)
            print('Clerk threw an elbow to your face!')

        if clerk_move == 'headbutt':
            your_health -= 15
            print('\n' * 30)
            print('Clerk headbutted you!')



    while True:
        sleep(2)
        print('\n' * 10)
        print(f'\n{set_color("FIGHT", red)}\n')
        print(f"Your health: {your_health}")
        print('\n' * 5)
        print(f"Clerk's health: {clerk_health}")
        print('\n' * 5)
        print('\nYour moves:\n1. Right Hook - 5dmg\n2. Uppercut - 7dmg\n3. Yeehaw Kimchi - 10dmg')
        move = input('Choose your move:')
        if move == '1':
            clerk_health -= your_attacks['right hook']
            print('\n' * 30)
            print(f"You threw a right hook!")
            sleep(1)
            clerk_move()
        if move == '2':
            clerk_health -= your_attacks['uppercut']
            print('\n' * 30)
            print(f"You land an uppercut!")
            sleep(1)
            clerk_move()
        if move == '3':
            clerk_health -= your_attacks['yeehaw kimchi']
            print('\n' * 30)
            print(f"You used your special move!")
            sleep(1)
            clerk_move()

        if your_health <= 0:
            inventory['misc'] = []
            inventory['disguise'] = []
            sleep(1)
            print('\n' * 30)
            print('You LOST. The clerk throws you out of his store...')
            break
        elif clerk_health <= 0:
            inventory['disguise'].append('The Disguise Kit')
            inventory['money'] += 500
            sleep(1)
            print('\n' * 30)
            print(f'You have {inventory["money"]} gold')
            print('YOU WON!!! You take the disguise kit as your reward and all of the clerk\'s money.\nYou walk back to the town square...')
            break
        else:
            continue


def ask_clerk():
    while True:
        print('\n')
        print('1. "I\'m looking for a disguise."')
        print('2. "I\'ve been wanting to change up my appearance."')
        print('3. "I would like to FIGHT"')
        ask_choice = input('What are you looking for?')
        if ask_choice == '1':
            sleep(2)
            print('\n' * 20)
            print('Clerk: "I mean, if you really really want one of those, we\'ve got em. But it\'s gonna cost ya."')
            sleep(2.5)
            print(
                '\nThe clerk walks to the back of the store and disappears for a minute or two...')
            sleep(5)
            print('He finally comes back with a disguise kit in his hands.')
            sleep(2)
            print(
                '\nClerk: Here is what we have. I\'m asking a fair bit, at 300 gold. Take it or leave it.')
            print('\n')
            print(f'Money: {inventory["money"]}')
            sleep(2)
            if not inventory['money'] >= 300:
                print(
                    'You don\'t have enough money! You thank the clerk for his time and walk back to the town square.')
                sleep(2)
                break
            else:
                print(f'You have {inventory["money"]} gold')
                buy_expensive_kit = input('Buy this disguise kit for 300 gold?:\n1. Yes\n2. No\n\nChoice:')
                if buy_expensive_kit == '1':
                    inventory['money'] -= 300
                    inventory['disguise'].append('The Disguise Kit')
                    print('\nYou bought the EXPENSIVE Disguise Kit! You big baller, you.')
                    print(f"\nAdded to Inventory: {inventory['disguise']}")
                    sleep(2)
                    break
                if buy_expensive_kit == '2':
                    print('You have made a wise financial decision. Congratulations!')
                    sleep(1)
                    break
                    
        if ask_choice == '2':
            sleep(2)
            print('\n' * 30)
            print('Clerk: "Well then, we\'ve got this nicely outfitted cosmetic section over here if you would like to have a look at the items."')
            sleep(2.5)
            print('\n' * 30)
            print('You immediately see in the makeup section of the store ✨ THE DISGUISE KIT ✨\nYou hold up the kit to the clerk and ask,\n"How much for this thing?"')
            sleep(4)
            print('\n' * 30)
            print('Clerk: Well, those things are pretty hard to come by nowadays. I\'d sell that to ya for 250 Gold...')
            sleep(3)
            if not inventory['money'] >= 250:
                print('You don\'t have enough money! You thank the clerk for his time and walk back to the town square.')
                sleep(2)
                break
            else: 
                print(f'You have {inventory["money"]} gold')
                buy_kit = input('Buy this disguise kit for 250 gold?:\n1. Yes\n2. No\n\nChoice:')
                if buy_kit == '1':
                    inventory['money'] -= 250
                    inventory['disguise'].append('The Disguise Kit')
                    print('\nYou bought the Disguise Kit!')
                    print(f"\nAdded to Inventory: {inventory['disguise']}")
                    sleep(2)
                    break
                if buy_kit == '2':
                    print('You decide to save your money.')
                    sleep(1)
                    break
        if ask_choice == '3':
            sleep(2)
            print('\n' * 30)
            print('Clerk: ...')
            sleep(2)
            print('\n' * 30)
            print('Clerk: "You... You what????"')
            sleep(2)
            print('\n' * 30)
            print('You deck the clerk square in the jaw and send him flying to the ground!')
            sleep(3)
            print('\n' * 30)
            print('To your surprise, he leaps back on his feet with blinding speed and raises his fists in some kind of foreign fighting stance.\nYou raise your fists and stare into his eyes menacingly...')
            sleep(3.5)
            fight_time()
            break


def sneaky_time():
    global sneaky
    clerk = ['at the register, looking around', 'wandering about, bored out of his mind', 'busy cleaning', 'busy restocking']
    player = ['the front of the store', 'the clothing aisle',
              'the food aisle', 'the makeup section']
    sneaky = True
    while sneaky:
        sneaky = True
        print(f'\n✨{set_color("SNEAKY TIME", yellow)}✨')
        clerk_spot = random.choice(clerk)
        player_spot = player[0]
        print('Sneaky time gives you an opportunity to steal things.\nYou can only steal when the clerk is busy.\nIf he is cleaning or restocking, he\'s not paying any attention to you...')
        print('\n' * 5)
        print(f'\nThe clerk is {clerk_spot}.')
        print(f'\nYou are at {player_spot}')
        choice = input(
            '\nWhat would you like to do?\n1: Wait for one minute\n2. Go to clothing aisle\n3. Go to food aisle\n4. Go to makeup section\n5. Leave\n\nChoice:')
        if choice == '1':
            sleep(2)
            print('\n' * 30)
            print('You wait for one minute...')
            sleep(5)
            continue

        # when the player enters a new location they need to have different options of what they could
        # possibly steal
        # depending on what the clerk is doing, they can be successful in stealing or get caught
        if choice == '2':
            player_spot = player[1]
            while True:
                clerk_spot = random.choice(clerk)
                sleep(2)
                print('\n' * 20)
                print(f'\nThe clerk is {clerk_spot}')
                print(f'\nYou are now at {player_spot}')
                choice_2 = input(
                    '\nWhat would you like to do?\n1: Wait for one minute\n2. Steal a hat\n3. Steal a fancy belt\n4. Go back to the front\n\nChoice:')
                if choice_2 == '1':
                    sleep(1)
                    print('\n' * 30)
                    print('You wait for one minute..')
                    sleep(5)
                    continue
                if choice_2 == '2':
                    if clerk_spot in ['busy cleaning', 'busy restocking']:
                        sleep(1)
                        print('\n' * 30)
                        print('You succeeded! You got the hat!')
                        inventory['misc'].append('hat')
                        print(f' Your Inventory: {", ".join(inventory["misc"])}')
                        continue
                    else:
                        get_caught()
                        break
                if choice_2 == '3':
                    if clerk_spot in ['busy cleaning', 'busy restocking']:
                        sleep(1)
                        print('\n' * 30)
                        print('You succeeded! You got the fancy belt!')
                        inventory['misc'].append('Fancy belt')
                        print(f' Your Inventory: {", ".join(inventory["misc"])}')
                        continue
                    else:
                        get_caught()
                        break
                if choice_2 == '4':
                    sleep(1)
                    print('\n' * 30)
                    print('You walk back to the front of the store.')
                    break
        if choice == '3':
            player_spot = player[2]
            while True:
                clerk_spot = random.choice(clerk)
                sleep(2)
                print('\n' * 30)
                print(f'\nThe clerk is {clerk_spot}')
                print(f'\nYou are now at {player_spot}')
                choice_3 = input(
                    '\nWhat would you like to do?\n1: Wait for one minute\n2. Steal some biscuits\n3. Steal some horse treats\n4. Go back to the front\n\nChoice:')
                if choice_3 == '1':
                    sleep(1)
                    print('\n' * 30)
                    print('You wait for one minute..')
                    sleep(5)
                    continue
                if choice_3 == '2':
                    if clerk_spot in ['busy cleaning', 'busy restocking']:
                        sleep(1)
                        print('\n' * 30)
                        print('You succeeded! You got the biscuits!')
                        inventory['misc'].append('biscuits')
                        print(f' Your Inventory: {", ".join(inventory["misc"])}')
                        continue
                    else:
                        get_caught()
                        break
                if choice_3 == '3':
                    if clerk_spot in ['busy cleaning', 'busy restocking']:
                        sleep(1)
                        print('\n' * 30)
                        print('You succeeded! You got the horse treats!')
                        inventory['misc'].append('horse treats')
                        print(f' Your Inventory: {", ".join(inventory["misc"])}')
                        continue
                    else:
                        get_caught()
                        break
                if choice_3 == '4':
                    sleep(1)
                    print('\n' * 30)
                    print('You walk back to the front of the store.')
                    break
        if choice == '4':
            player_spot = player[3]
            while True:
                clerk_spot = random.choice(clerk)
                sleep(2)
                print('\n' * 30)
                print(f'\nThe clerk is {clerk_spot}')
                print(f'\nYou are now at {player_spot}')
                choice_4 = input(
                    '\nWhat would you like to do?\n1: Wait for one minute\n2. Steal some lipstick\n3. Steal The Disguise Kit\n4. Go back to the front\n\nChoice:')
                if choice_4 == '1':
                    sleep(1)
                    print('\n' * 30)
                    print('You wait for one minute..')
                    sleep(5)
                    continue
                if choice_4 == '2':
                    if clerk_spot in ['busy cleaning', 'busy restocking']:
                        sleep(1)
                        print('\n' * 30)
                        print('You succeeded! You got the lipstick!')
                        inventory['misc'].append('liptstick')
                        print(f' Your Inventory: {", ".join(inventory["misc"])}')
                        continue
                    else:
                        get_caught()
                        break
                if choice_4 == '3':
                    if clerk_spot in ['busy cleaning', 'busy restocking']:
                        sleep(1)
                        print('\n' * 30)
                        print('You succeeded! You got The Disguise Kit!')
                        inventory['disguise'].append('The Disguise Kit')
                        print(f' Your Inventory: {", ".join(inventory["disguise"])}')
                        continue
                    else:
                        get_caught()
                        break
                if choice_4 == '4':
                    sleep(1)
                    print('\n' * 30)
                    print('You walk back to the front of the store.')
                    break
        if choice == '5':
            break


def store_loop():
    while True:
        sleep(2)
        print('\n' * 20)
        print("""You walk inside of the store and take a quick look around. 
It's quite cluttered on the inside, filled with equal amounts of junk and seemingly valuble items. 
You are approached by the store clerk.""")
        sleep(6)
        print('\n' * 20)
        print('Clerk: "Hey there mister! How ya doing this fine day?"')
        print('\n')
        print('1. "I\'m doing fine, how are you?"')
        print('2. "Good. What all do you have here?"')
        print('3. Don\'t say anything to the clerk.')
        print('4. Leave.')
        converse_choice = input('What do you want to say?: ')
        if converse_choice == '1':
            sleep(1)
            print('\n' * 20)
            print('Clerk: "I\'m just dandy, thank you for asking!')
            print('Can I help ya find anything?"')
            ask_clerk()
            break
        if converse_choice == '2':
            sleep(1)
            print('\n' * 20)
            print("""Clerk: 'Well, we have just about anything a fine, respectable person as yourself may want! 
From food to clothes to guns to saddles, we have it all.'""")
            ask_clerk()
            break
        if converse_choice == '3':
            sleep(1)
            print('\n' * 20)
            print('Clerk: "Huh, well if you ever need anything just ask me."')
            print(
                'The clerk walks away from you and starts minding his own business.')
            sleep(3.5)
            sneaky_time()
            break
        if converse_choice == '4':
            break
