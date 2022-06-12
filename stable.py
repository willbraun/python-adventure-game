from re import X
from time import sleep
import random
from pip import main
from general import *

board = [' ' for x in range(10)]

def choose_square(mark, position):
    board[position] = mark

def open_space(position):
    return board[position] == ' '

def print_board(board):
    print('1  |2  |3')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('4  |5  |6')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('7  |8  |9')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def winner(bo, ma):
    return (bo[7] == ma and bo[8] == ma and bo[9] == ma) or (bo[4] == ma and bo[5] == ma and bo[6] == ma) or(bo[1] == ma and bo[2] == ma and bo[3] == ma) or(bo[1] == ma and bo[4] == ma and bo[7] == ma) or(bo[2] == ma and bo[5] == ma and bo[8] == ma) or(bo[3] == ma and bo[6] == ma and bo[9] == ma) or(bo[1] == ma and bo[5] == ma and bo[9] == ma) or(bo[3] == ma and bo[5] == ma and bo[7] == ma)

def user_move():
    run = True
    while run:
        print("\n"*5)
        move = input(f'{set_color("Stable Master", red)}: Picka square an\' mark it with \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if open_space(move):
                    run = False
                    choose_square('X', move)
                else:
                    print("\n"*2)
                    print(f'{set_color("Stable Master", red)}: I dun picked that one!')
            else:
                print("\n"*2)
                print(f'{set_color("Stable Master", red)}: Pick 1 through 9!')
        except:
            print("\n"*2)
            print('Please type a number!')

def computer_move():
    possibleMoves = [x for x, mark in enumerate(board) if mark == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if winner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = random_selection(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = random_selection(edgesOpen)
        
    return move

def random_selection(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def the_end():
    sleep(10)
    print("\n"*10)
    print('  ........::::::::::::..           .......|...............::::::::........')
    print('     .:::::;;;;;;;;;;;:::::.... .     \   | ../....::::;;;;:::::.......')
    print('         .        ...........   / \\_   \  |  /     ......  .     ........./\ ')
    print("...:::../\\_  ......       ..._/'   \\\_  \###/   /\_    .../ \_.......   _// \ ")
    print(".::::./   \\\ _   .../\      /'      \\\\#######//   \/\   //   \_   ....////   \ ")
    print("    _/      \\\\    _/ \\\   /            \\\\###////      \////   \__  _/////     \ ")
    print("  ./          \\\ /    \ /                \//////                 \/////")
    print("  /              \\/                       \                         ////    ")
    print("")
    print("        x               X                      X  x             ")
    print("     x  X  X            X                      X  x           X  x")
    print("     xxxXxxX         x  X  X                   Xx        x    X  x")
    print("        X             xXXxxx                   X          xxXXxXx ")
    print("--------x---------------x-----------------*----x-------------x---------------")
    print(" ")
    print(" ")
    sleep(3)
    print("\n"*3)
    print("You leave Durango just as that Colorado sun starts creeping down behind the mountains. ")
    sleep(3)
    print("\n"*2)
    print("Sometimes freedom is given and sometimes it's earned. Today you earned it.")
    sleep(3)
    print("\n"*2)
    print("It's a long and dusty 90 miles to the next town and you've got a lot more adventuring ahead of you -- you might as well get some rest.")
    sleep(6)
    print("\n"*2)    
    print("You tilt your hat down over your eyes and let the stagecoach rock you to sleep.")
    sleep(5)
    print("\n"*5)  
    print("- -   The End   - - ")
    print('\n'*5)
    sleep(10)
    exit()

def coin_flip():
    while True:
        print(f'{set_color("Stable Master", red)}: Yur choice, call it in the air: heads or tails?')
        print("He flips the coin- ")
        sleep(2)
        print("\n"*5)
        guess = input("1: 'heads'\n2: 'tails'\n\nChoice: ")
        if(guess == "1"):
            print("\n 'I choose heads'")
        elif(guess == "2"):
            print("\n 'I choose tails.'")
        else:
            print(f'\n{set_color("Stable Master", red)}: That ain\'t no choice!!')
        flip = random.choice(["1", "2"])
        
        if(flip == "1"):
                sleep(2)
                print("\nThe coin hits the ground - on heads")
        else:
                sleep(2)
                print("\nThe coin hits the ground - on tails")
        
        if(flip == guess):
                sleep(2)
                print(f'\n{set_color("Stable Master", red)}: You won ... I guess I misjudged ya. Here\'s yer ticket for the stage coach.')
                the_end()
        else:
            sleep(2)
            print(f'\n{set_color("Stable Master", red)}: Ha! Not so lucky for you huh? I\'ll tell ya what. I\'ll give you another chance.')
            ttt_game()                  


def ttt_game():
        sleep(5)
        print("\n"*5)
        print(f'{set_color("Stable Master", red)}: It\'s the wildest game in the West - it\'s called: Tic Tac Toe!')
        sleep(5)
        print('\n'*5)
        global board
        board = [' ' for x in range(10)]
        print_board(board)

        while not(isBoardFull(board)):
            if not(winner(board, 'O')):
                user_move()
                print("\n"*2)
                print_board(board)
            else:
                print(f'{set_color("Stable Master", red)}: Haha! I win! Tell ya what, that was so much fun I\'ll give ya another go at it.')
                break

            if not(winner(board, 'X')):
                move = computer_move()
                if move == 0:
                    sleep(2)
                    print("\n"*2)
                    print(f'{set_color("Stable Master", red)}: Tie game?? Drats! Well... how about a different game? This is the second wildest game in the West. It\'s called: flip-a-coin!')
                    sleep(5)
                    print("\n"*5)
                    coin_flip()
                else:
                    choose_square('O', move)
                    print("\n"*2)
                    sleep(3)
                    print(f'{set_color("Stable Master", red)}: Let\'s see... Imma pick', move,': ')
                    print("\n"*2)
                    sleep(3)
                    print_board(board)
            else:
                print(f'{set_color("Stable Master", red)}: You won ... I guess I misjudged ya. Here\'s yer ticket for the stage coach.')
                the_end()

            

        while True:
            answer = input(f'{set_color("Stable Master", red)}: Ya wanna play again??\'\n1: Yes\n2: No (this will end your game)\n\nChoice: ')
            if answer == "1":
                board = [' ' for x in range(10)]
                ttt_game()
            else:
                exit()



def stable_loop():
    if not "The Disguise Kit" in inventory["disguise"]:
        sleep(2)
        print('\n' * 20)
        print("You enter the stable. You see the stable master working, his back is turned")
        while True:

            choice = input("Would you like to: \n1: Speak to the stable master\n2: Steal his horse while he isn't looking\n3: Leave\n\nChoice: ")
            if choice == "1":
                    sleep(2)
                    print('\n' * 5)
                    print("You approach the stable master. He seems shocked to see you even you before you speak. You ask him about buying a horse.")
                    print(']n'* 2)
                    print(f'{set_color("Stable Master", red)}: I recognize you!! I\'d be hung for selling a horse to a known criminal! Now leave!')
                    sleep(5)
                    print("\n"*5)
                    print("You leave.")
                    sleep(3)
                    break
            if choice == "2":
                    sleep(2)
                    print('\n' * 5)
                    print("You approach the horse, moving as quietly as you can. As you lift yourself onto the saddle you spook the horse, causing it to buck. The noise alerts the stable master, who is ready with his six-shooter. A few quick shots and you're dead.")
                    sleep(10)
                    print('\n' * 2)
                    print("Game Over.") 
                    start_again = input("1: Start Over in the town square\n2: Exit\n\nChoice: ")
                    if start_again == "1":
                        break
                    elif start_again == "2":
                        exit()
                    else:
                        print("That's not a choice")
            if choice == "3":
                print("\n"*5)
                break
    else:    
                sleep(3)
                print('\n' * 20)
                print("You enter the stable. The stable master sees you and approaches.")
                sleep(5)
                print("\n"*5)
                print(f'{set_color("Stable Master", red)}: Well, I\'ve never seen you around here before.  You must be new in town. How can I help you?')
                while True:
                    sleep(5)
                    print("\n"*3)
                    print("'I need a ticket for the first stagecoach leaving town.'")
                    sleep(5)
                    print("\n"*3)
                    print(f'{set_color("Stable Master", red)}: Leaving so soon? Can\'t say I blame you. Problem is the next stage coach is all full up but I uh... I\'d be willin\' to toss somebody off and give your their seat for .... say ... $500')
                    if inventory['money'] >= 500:
                        print("\n"*3)
                        print("You pay the Stable Master the $500 - his eyes bulge at the sight")
                        print(f'{set_color("Stable Master", red)}: Wow, high roller - you must\'ve done good at the faro table... ')
                        print("\n"*2)
                        sleep(2)
                        print("The Stable Master hands you a ticket for the stagecoach.")
                        sleep(5)
                        the_end()
                    else:
                        sleep(5)
                        print("\n"*3)
                        print("'I don't have $500...'")
                        sleep(5)
                        print(f'{set_color("Stable Master", red)}: Well, how about a game - a game of chance and strategy?')
                        print("\n"*3)
                        print("'I'm listening...'")
                        ttt_game()
