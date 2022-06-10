from time import sleep
import random
from inventory import inventory

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
# if the clerk is not cleaning or busy, he is at the register, keeping a watchful eye on you.
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
            sleep(2)
            print(
                '\nThe clerk walks to the back of the store and disappears for a minute or two...')
            sleep(5)
            print('He finally comes back with a disguise kit in his hands.')
            sleep(2)
            print(
                '\nClerk: Here is what we have. I\'m asking a fair bit, at 300 gold. Take it or leave it.')
            print('\n')
            print(inventory['money'])
            if not inventory['money'] >= 300:
                print(
                    'You have no money! You thank the clerk for his time and walk back to the town square.')
                sleep(2)
                break
            else:
                pass


def sneaky_time():
    global sneaky
    clerk = ['at the register, looking around', 'wandering about, bored out of his mind', 'busy cleaning', ' busy restocking']
    player = ['the front of the store', 'the clothing aisle',
              'the food aisle', 'the makeup section']
    sneaky = True
    while sneaky:
        sneaky = True
        clerk_spot = random.choice(clerk)
        player_spot = player[0]
        print('\n' * 30)
        print(f'\nThe clerk is {clerk_spot}.')
        print(f'\nYou are at {player_spot}')
        choice = input(
            '\nWhat would you like to do?\n1: Wait for one minute\n\n2. Go to clothing aisle\n3. Go to food aisle\n4. Go to makeup section\n\nChoice:')
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
                print('\n' * 30)
                print(f'\nThe clerk is {clerk_spot}')
                print(f'\nYou are now at {player_spot}')
                choice_2 = input(
                    '\nWhat would you like to do?\n1: Wait for one minute\n\n2. Steal a hat\n3. Steal a fancy belt\n4. Go back to the front\n\nChoice:')
                if choice_2 == '1':
                    sleep(1)
                    print('\n' * 30)
                    print('You wait for one minute..')
                    sleep(5)
                    continue
                if choice_2 == '2':
                    if clerk_spot == 'busy cleaning' or clerk_spot == 'busy restocking':
                        sleep(1)
                        print('\n' * 30)
                        print('You succeeded! You got the hat!')
                        inventory['misc'].append('hat')
                        print(inventory['misc'])
                        continue
                    else:
                        get_caught()
                        break
                if choice_2 == '3':
                    if clerk_spot == 'busy cleaning' or clerk_spot == 'busy restocking':
                        sleep(1)
                        print('\n' * 30)
                        print('You succeeded! You got the fancy belt!')
                        inventory['misc'].append('Fancy belt')
                        print(inventory['misc'])
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
                    '\nWhat would you like to do?\n1: Wait for one minute\n\n2. Steal some biscuits\n3. Steal some horse treats\n4. Go back to the front\n\nChoice:')
                if choice_3 == '1':
                    sleep(1)
                    print('\n' * 30)
                    print('You wait for one minute..')
                    sleep(5)
                    continue
                if choice_3 == '2':
                    if clerk_spot == 'busy cleaning' or clerk_spot == 'busy restocking':
                        sleep(1)
                        print('\n' * 30)
                        print('You succeeded! You got the biscuits!')
                        inventory['misc'].append('biscuits')
                        print(inventory['misc'])
                        continue
                    else:
                        get_caught()
                        break
                if choice_3 == '3':
                    if clerk_spot == 'busy cleaning' or clerk_spot == 'busy restocking':
                        sleep(1)
                        print('\n' * 30)
                        print('You succeeded! You got the horse treats!')
                        inventory['misc'].append('horse treats')
                        print(inventory['misc'])
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
                    '\nWhat would you like to do?\n1: Wait for one minute\n\n2. Steal some lipstick\n3. Steal The Disguise Kit\n4. Go back to the front\n\nChoice:')
                if choice_4 == '1':
                    sleep(1)
                    print('\n' * 30)
                    print('You wait for one minute..')
                    sleep(5)
                    continue
                if choice_4 == '2':
                    if clerk_spot == 'busy cleaning' or clerk_spot == 'busy restocking':
                        sleep(1)
                        print('\n' * 30)
                        print('You succeeded! You got the lipstick!')
                        inventory['misc'].append('liptstick')
                        print(inventory['misc'])
                        continue
                    else:
                        get_caught()
                        break
                if choice_4 == '3':
                    if clerk_spot == 'busy cleaning' or clerk_spot == 'busy restocking':
                        sleep(1)
                        print('\n' * 30)
                        print('You succeeded! You got The Disguise Kit!')
                        inventory['disguise'].append('The Disguise Kit')
                        print(inventory['disguise'])
                        continue
                    else:
                        get_caught()
                        break
                if choice_4 == '4':
                    sleep(1)
                    print('\n' * 30)
                    print('You walk back to the front of the store.')
                    break









def store_loop():
    while True:
        sleep(2)
        print('\n' * 20)
        print("""You walk inside of the store and take a quick look around. 
It's quite cluttered on the inside, filled with equal amounts of junk and seemingly valuble items. 
You are approached by the store clerk.""")
        sleep(1)
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
            sleep(2)
            sneaky_time()
            break
