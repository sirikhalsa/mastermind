# This is a python implementation of the mastermind game using the terminal as an interface.

from random import randint

def greeting():
    print('Welcome to Mastermind!\nThe computer will generate a secret code and it will be your job to decipher the code in as few guesses as possible!')

def build_code(size):
    code = []
    rand_list = [randint(0,9) for i in range(20)]
    while len(code) < size:
        if rand_list[-1] not in code:
            code.append(rand_list.pop())
        else:
            rand_list.pop()
    return code

def difficulty_selection():
    size = int(input('\nWhat difficulty level would you like to play?\nPlease input the appropriate number:\n1) Easy\n2) Normal\n3) Hard\n->'))
    if size == 1:
        secret_code = build_code(4)
    elif size == 2:
        secret_code = build_code(5)
    elif size == 3:
        secret_code = build_code(6)
    else:
        print('Incorrect input, let\'s try that again..,')
        difficulty_selection()
    # print(secret_code)
    return secret_code

def get_player_guess():
    player_guess = input('\nPlease input a guess for the secret code:\n->')
    return player_guess

def play_game(secret_code):
    blank_guess_list = ['_' for i in range(len(secret_code))]
    last_guess_list = ['_' for i in range(len(secret_code))]
    guess_count = 0
    print('The secret code is: {}'.format(blank_guess_list))
    while last_guess_list != secret_code:
        if guess_count > 0:
            print('Your last guess was:\n{}'.format(last_guess_list))
        last_guess_list = ['_' for i in range(len(secret_code))]
        player_guess = get_player_guess()
        if len(player_guess) != len(secret_code):
            print('Incorrect code length, please try again...')
            player_guess = get_player_guess()
        player_guess_list = [int(i) for i in player_guess]
        last_guess_accuracy = ['_' for i in range(len(secret_code))]
        for i in range(len(player_guess_list)):
            if player_guess_list[i] == secret_code[i]:
                last_guess_list[i] = secret_code[i]
                # last_guess_accuracy[i] = 'G'
            elif player_guess_list[i] in secret_code:
                last_guess_list[i] = '[{}]'.format(player_guess_list[i])
                # last_guess_accuracy[i] = 'O'
            # else:
            #     last_guess_accuracy[i] = 'R'
        guess_count += 1
    if guess_count == 1:
        print('Incredible! You deciphered the code {} on your first guess!'.format(secret_code))
    elif guess_count > 1:
        print('Congratulations! You deciphered the secret code {}! It only took you {} guesses!'.format(secret_code, guess_count))

def play_again():
    restart = input('\nWould you like to play again? yes (y) or no (n)\n->')
    if restart == 'y':
        execute(True)
    else:
        goodbye()

def goodbye():
    print('Thank you for playing Mastermind! Good bye!')

def execute(played = False):
    if not played:
        greeting()
    player_code = difficulty_selection()
    play_game(player_code)
    play_again()

execute()
