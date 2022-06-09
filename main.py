import saloon
import store
import stable
from inventory import inventory


# print description of how we ended up in the two square

while True:
    print('\n' * 10)
    question = input("You're in the town square. Where do you want to go? 1: Saloon, 2: Store, 3: Stable: ")
    if question == '1':
        saloon.saloon_loop()
    elif question == '2':
        store.store_loop()
    elif question == '3':
        stable.stable_loop()
    else:
        break
