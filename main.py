import saloon
import store
import stable
from time import sleep
from general import *

# print description of how we ended up in the two square
print("-------------------------------")
print('\n'*20)
print('The harsh Colorado sunlight stings your eyes - but you welcome the stinging because it\'s the first sunlight you\'ve seen in days.')
sleep(6)
print('\n'*1)
print('You\'ve been in the town jail cell long enough and that sunlight means freedom.')
sleep(6)
print('\n'*1)
print('There are two things you know for sure: the first is when opportunity knocks you have to answer --- so when that forgetful sheriff left your cell door unlocked before taking his afternoon nap you answered.')
sleep(6)
print('\n'*1)
print('The second thing you know: you\'ve got to...')
sleep(3)
print("  _____ ____   ____    _    ____  _____     _____ ____   ___  __  __     ____  _   _ ____      _    _   _  ____  ___  _ ")
print(" | ____/ ___| / ___|  / \  |  _ \| ____|   |  ___|  _ \ / _ \|  \/  |   |  _ \| | | |  _ \    / \  | \ | |/ ___|/ _ \| |")
print(" |  _| \___ \| |     / _ \ | |_) |  _|     | |_  | |_) | | | | |\/| |   | | | | | | | |_) |  / _ \ |  \| | |  _| | | | |")
print(" | |___ ___) | |___ / ___ \|  __/| |___    |  _| |  _ <| |_| | |  | |   | |_| | |_| |  _ <  / ___ \| |\  | |_| | |_| |_|")
print(" |_____|____/ \____/_/   \_\_|   |_____|   |_|   |_| \_\\___/|_|   |_|   |____/ \___/|_| \_\/_/   \_\_| \_|\____|\___/(_)")
print("                                                                                                                        ")

sleep(3)
print("\n --- and fast!!")

sleep(6)
print('\n'*5)
print("Looking across the town's muddy, horse trodden thoroughfare you see three buildings you can enter: the saloon, the general store and the horse stable. ")

while True:
    question = input("\n Where do you want to go?\n1: Saloon\n2: Store\n3: Stable\n\nChoice: ")
    if question == '1':
        saloon.saloon_loop()
    elif question == '2':
        store.store_loop()
    elif question == '3':
        stable.stable_loop()
    else:
        break
