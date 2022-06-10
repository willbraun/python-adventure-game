inventory = { 'money': 100, 'disguise': [], 'food': [], 'misc': []}

can_count_cards = False

red = '\033[1;31;40m'
green = '\u001b[32m'
yellow = '\033[1;33;40m'
purple = '\033[1;35;40m'

def set_color(word, color):
    return f"{color}{word}\033[0;0m"