
def buy_drink():
    print('\n' * 8)
    print('You enter the saloon, you go up to the bartender and check the menu.')
    choice = input('Pick a drink from the menu: 1: Beer, 2: Whiskey, 3: Margarita.')
    if choice == '1':
        print('You guzzle your hipstery IPA down like a fish out of water.')
    if choice == '2':
        print('You throw back the entire bottle of whiskey in three satisfying gulps.')
    if choice == '3':
        print('You sip on your Margarita like the classy scoundrel you are.')

def saloon_loop():
    while True:
        buy_drink()