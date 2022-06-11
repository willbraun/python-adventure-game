inventory = { 'money': 100, 'disguise': [], 'food': [], 'misc': []}

can_count_cards = False

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'

def set_color(text, color):
    return f"{color}{text}\033[0;0m"