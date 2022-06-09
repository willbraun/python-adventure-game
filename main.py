import saloon
import store
import stable
from inventory import inventory

inventory = { 'money': 0, 'disguise': None }

# print description of how we ended up in the two square

while True:

    question = input("You're in the town square. Where do you want to go?\n1: Saloon\n2: Store\n3: Stable\n\nChoice: ")
    if question == '1':
        saloon.saloon_loop()
    elif question == '2':
        store.store_loop()
    elif question == '3':
        stable.stable_loop()
    else:
        break
