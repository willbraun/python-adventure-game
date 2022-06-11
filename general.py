inventory = { 'money': 100, 'disguise': [], 'food': [], 'misc': []}

can_count_cards = False

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m' # cloaked woman
blue = '\033[34m' # old man
purple = '\033[35m' # store clerk
cyan = '\033[36m' # faro dealer
bright_green = '\u001b[32;1m' # bartender
bright_magenta = '\u001b[35;1m' # town drunk

def set_color(text, color):
    return f"{color}{text}\033[0;0m"