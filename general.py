inventory = { 'money': 100, 'disguise': [], 'food': [], 'misc': []}

red = '\033[1;31;40m'
green = '\u001b[32m'

def red(word):
    return f"\033[1;31;40m{word}\033[0;0m"

def set_color(word, color):
    return f"{color}{word}\033[0;0m"