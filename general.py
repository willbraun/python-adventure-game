inventory = { 'money': 100, 'disguise': [], 'food': [], 'misc': []}

can_count_cards = False

red = '\033[31m'
green = '\u001b[32m'
yellow = '\033[33m'
purple = '\033[35m'

def set_color(word, color):
    return f"{color}{word}\033[0;0m"