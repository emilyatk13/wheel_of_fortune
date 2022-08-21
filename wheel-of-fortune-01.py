from config import wheel_text_loc
from config import word_list_loc
from config import round_3_word_list_loc

import random

print('''\n=================================================================================================================
                                        Welcome to the Wheel of Fortune! 
We will play this game in three rounds. 
During the first two rounds, a starting player will be randomly selected. 
The player can either spin the wheel, buy a vowel for $250, or guess the word. 
The person who correctly guesses the word wins the round and keeps their prize money! 
Round one and two work the same way. The person with the most money at the end of the first two rounds will play in Round 3. 
Enter your player names to begin!
=================================================================================================================''')

round = 1
word_list = []
round_3_word_list = []
wheel_values = []
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']
players={0:{'roundtotal':0,'gametotal':0,'name':''},
         1:{'roundtotal':0,'gametotal':0,'name':''},
         2:{'roundtotal':0,'gametotal':0,'name':''},
        }


# gets wheel values from wheel_data.txt, prints values into wheel_values list
def get_wheel_values(wheel_values):
    with open(wheel_text_loc, 'r') as wheel_options:
        lines_wheel=wheel_options.readlines()
    for l in lines_wheel:
        as_list_wheel = l.split(', ')
        wheel_values.append(as_list_wheel[0].replace('\n', ''))

get_wheel_values(wheel_values)

# gets word list from word_list.txt, prints values into word_list list
def get_word_list(word_list):
    with open(word_list_loc, 'r') as word_options:
        lines_word=word_options.readlines()
    for l in lines_word:
        as_list_words = l.split(', ')
        word_list.append(as_list_words[0].replace('\n', ''))

get_word_list(word_list)

# gets list of words for round 3
# I wanted these to be a little longer since we have to display letters!
def get_round_3_word_list(round_3_word_list):
    with open(round_3_word_list_loc, 'r') as round_3_word_options:
            lines_word_3=round_3_word_options.readlines()
    for l in lines_word_3:
        as_list_words_3 = l.split(', ')
        round_3_word_list.append(as_list_words_3[0].replace('\n', ''))

get_round_3_word_list(round_3_word_list)

# user input for player names, adds to dictionary
def get_player_names(players):
    player_1_name = input('\nPlease enter the name for Player 1: ')
    players[0]['name'] = player_1_name
    player_2_name = input('\nPlease enter the name for Player 2: ')
    players[1]['name'] = player_2_name
    player_3_name = input('\nPlease enter the name for Player 3: ')
    players[2]['name'] = player_3_name

#get_player_names(players)

#function to pick a random player, will probably need to expand functionality to keep track
def get_player(players):
    global init_player
    init_player = random.choice(list(players.keys()))
    return init_player

# fucntion to pick random word
def get_word(word_list):
    global correct_word
    global display_word
    correct_word = random.choice(word_list)
    display_word = '_'*len(correct_word)
    return correct_word, display_word

# function to pick random wheel value
#def get_wheel_return(wheel_values):
 #   global wheel_return
  #  wheel_return = random.choice(wheel_values)
   # return wheel_return

#round setup, picks the word, initial player, resets all player roundtotal back to 0
def get_round_setup(word_list, players, get_player, get_word):
    get_word(word_list)
    get_player(players)
    for i in players:
        players[i]['roundtotal'] = 0

#get player for final round
def get_round_3_player(players):
    global highest_amount
    player_1_amount = int(players[0]['gametotal'])
    player_2_amount = int(players[1]['gametotal'])
    player_3_amount = int(players[2]['gametotal'])
    highest_amount = max(player_1_amount,player_2_amount,player_3_amount)
    round_3_player_list = [i for i in players if players[i]['gametotal']==highest_amount]
    round_3_player = round_3_player_list[0]
    round_3_player_name = players[round_3_player]['name']
    print(f'\n=========== Welcome to Round 3! ===========\n{round_3_player_name}, you ended the first two rounds with the highest winnings at ${highest_amount}! Good luck!')

# get word/display word for final round
def get_round_3_word(round_3_word_list):
    global round_3_correct_word
    global round_3_display_word
    round_3_correct_word = random.choice(round_3_word_list)
    letters_to_show = ['r', 's', 't', 'l', 'n', 'e']
    list_word = list(round_3_correct_word)
    for i in range(len(list_word)):
        if list_word[i] not in letters_to_show:
            list_word[i] = '_'
    round_3_display_word = ''.join(list_word)

# beginning of round process
get_player_names(players)
in_play = True
while in_play == True:
    if round <= 2:
        get_round_setup(word_list, players, get_player, get_word)
        current_player = init_player
        print(f'\n=========== Welcome to Round {round}! ===========')
        correct_word_guessed = False
        while correct_word_guessed == False:
            still_in_turn = True
            while still_in_turn == True:
                current_player_name = players[current_player]['name']
                current_round_total = int(players[current_player]['roundtotal'])
                print(f'\n{current_player_name}, it\'s your turn! You currently have ${current_round_total}.')
                player_choice = input(f'\n{current_player_name}, would you like to [s]pin the wheel, [b]uy a vowel, or [g]uess the answer? ')
                if player_choice == 's':
                    global wheel_return
                    wheel_return = random.choice(wheel_values)
                    if wheel_return == '1':
                        print(f'\nYou spun the wheel and it landed on BANKRUPT. Sorry, you lost your turn and your money from this round. Better luck next time!')
                        players[current_player]['roundtotal'] = 0
                        still_in_turn = False
                        break
                    if wheel_return == '2':
                        print(f'\nYou spun the wheel and it landed on LOSE TURN. Sorry, you lost your turn. Better luck next time!')
                        still_in_turn = False
                        break
                    else:
                        print(f'\nYou spun the wheel and it landed on ${wheel_return}!')
                        correct_letter = False
                        while correct_letter == False:
                            print(f'\n{display_word}')
                            #remove this for final version
                            global guess
                            guess = input('\nGuess a letter! ')
                            if guess in vowels:
                                print('\nError:\nYou must guess a consonant. Try again.')
                                continue
                            if guess in display_word:
                                print(f'\nError:\n{guess} has already been guessed. Try again.')
                                continue
                            if len(guess) > 1:
                                print(f'\nError:\nYou may only guess one letter at a time. Try again.')
                                continue
                            if guess not in correct_word:
                                print(f'\nSorry, that letter is not in the word.')
                                still_in_turn = False
                                break
                            i = 0
                            if guess in correct_word:
                                while correct_word.find(guess, i) != -1:
                                    i = correct_word.find(guess, i)
                                    display_word = display_word[:i] + guess + display_word[i+1:]
                                    i += 1
                                print(f'\n{display_word}')
                                current_round_total = int(players[current_player]['roundtotal'])
                                wheel_return_int = int(wheel_return)
                                new_round_total = current_round_total + wheel_return_int
                                players[current_player]['roundtotal'] = new_round_total
                                print(f'\nCorrect guess! You have earned ${wheel_return}!')
                                player_round_total = players[current_player]['roundtotal']
                                correct_letter = True
                            if correct_word == display_word:
                                # TODO create variable for winner
                                # TODO add message displaying $
                                current_round_total = int(players[current_player]['roundtotal'])
                                wheel_return_int = int(wheel_return)
                                new_round_total = current_round_total + wheel_return_int
                                current_game_total = int(players[current_player]['gametotal'])
                                new_game_total = current_game_total + new_round_total
                                players[current_player]['gametotal'] = new_game_total
                                print(f'\n{current_player_name}, you win this round! The word was {correct_word}.')
                                print(f'\nYou now have ${new_game_total} in the bank!')
                                correct_word_guessed = True
                                still_in_turn = False
                if player_choice == 'b':
                    current_round_total = int(players[current_player]['roundtotal'])
                    if current_round_total < 250:
                        print('\nError:\nYou don\'t have enough money. Please choose another option.')
                        continue
                    if current_round_total > 250:
                        correct_letter = False
                        while correct_letter == False:
                            print(f'\n{display_word}')
                            #remove this for final version
                            guess = input('\nGuess a vowel! ')
                            if guess in consonants:
                                print('\nError:\nIf you would like to guess a consonant, spin the wheel. Try again.')
                                continue
                            if guess in display_word:
                                print(f'\nError:\n{guess} has already been guessed. Try again.')
                                continue
                            if len(guess) > 1:
                                print(f'\nError:\nYou may only guess one letter at a time. Try again.')
                                continue
                            if guess not in correct_word:
                                print(f'\nSorry, that letter is not in the word.')
                                still_in_turn = False
                                break
                            i = 0
                            if guess in correct_word:
                                while correct_word.find(guess, i) != -1:
                                    i = correct_word.find(guess, i)
                                    display_word = display_word[:i] + guess + display_word[i+1:]
                                    i += 1
                                print(f'\n{display_word}')
                                new_round_total = current_round_total - 250
                                players[current_player]['roundtotal'] = new_round_total
                                print(f'\nCorrect guess!')
                                player_round_total = players[current_player]['roundtotal']
                                correct_letter = True
                            if correct_word == display_word:
                                new_round_total = current_round_total - 250
                                current_game_total = int(players[current_player]['gametotal'])
                                new_game_total = current_game_total + new_round_total
                                players[current_player]['gametotal'] = new_game_total
                                print(f'\n{current_player_name}, you win this round! The word was {correct_word}.')
                                print(f'\nYou now have ${new_game_total} in the bank!')
                                correct_word_guessed = True
                                still_in_turn = False
                if player_choice == 'g':
                    print(f'\n{display_word}')
                    guess = input('\nGuess the word! ')
                    if guess == correct_word:
                        print(f'\n{current_player_name}, you win this round! The word was {correct_word}.')
                        current_round_total = int(players[current_player]['roundtotal'])
                        current_game_total = int(players[current_player]['gametotal'])
                        new_game_total = current_game_total + current_round_total
                        players[current_player]['gametotal'] = new_game_total
                        print(f'\nYou now have ${new_game_total} in the bank!')
                        correct_word_guessed = True
                        still_in_turn = False
                    if guess != correct_word:
                        print(f'\nSorry, {guess} is not the correct answer.')
                        still_in_turn = False
            current_player = (current_player +1) % len(players)
    round = round + 1
    if round == 3:
        get_round_3_player(players)
        get_round_3_word(round_3_word_list)
        print('\nDuring Round 3, you will see a word with the letters \'RSTLNE\' filled in. You get 4 guesses: 3 consonants and one vowel. We\'ll let you know if your guess is correct, but we won\'t let you know where the letter goes. After 4 guesses, you\'ll have a chance to guess the word. If you get it right, congrats! If not, no prize money for you. Good luck!')
        print(f'\n{round_3_display_word}')
        round_3_letter_guesses = 0
        round_3_in_play = True
        while round_3_in_play == True:
            round_3_guessing = True
            while round_3_guessing == True:
                if round_3_letter_guesses <= 2:
                    round_3_guess = input('\nGuess a consonant to reveal if it\'s in the word: ')
                    if round_3_guess in vowels:
                        print(f'\nYou may only guess consonants at this time. Please try again.')
                        continue
                    if round_3_guess in round_3_correct_word:
                        print(f'\nCorrect! {round_3_guess} is in the word. Time to guess your next letter!')
                        break
                    if round_3_guess not in round_3_correct_word:
                        print(f'\nSorry! {round_3_guess} is not in the word. Better luck on your next try!')
                        break
                if round_3_letter_guesses == 3:
                    round_3_guess = input('\nGuess a vowel to reveal if it\'s in the word: ')
                    if round_3_guess in consonants:
                        print(f'\nYou may only guess vowels at this time. Please try again.')
                        continue
                    if round_3_guess in round_3_correct_word:
                        print(f'\nCorrect! {round_3_guess} is in the word. Time to guess the word!')
                        break
                    if round_3_guess not in round_3_correct_word:
                        print(f'\nSorry! {round_3_guess} is not in the word. Better luck on your next try!')
                        break
                if round_3_letter_guesses == 4:
                    round_3_final_guess = input('\nTime to guess the word! ')
                    if round_3_final_guess == round_3_correct_word:
                        total_winnings = highest_amount + 1000
                        print(f'\nCorrect, the word was {round_3_correct_word}!! You WIN $1,000, bringing your total winnings to ${total_winnings}.')
                        round_3_guessing = False
                        round_3_in_play = False
                        in_play = False
                    if round_3_final_guess != round_3_correct_word:
                        print('\nSorry, that wasn\'t the correct word. Better luck next time!')
                        round_3_guessing = False
                        round_3_in_play = False
                        in_play = False
            round_3_letter_guesses = round_3_letter_guesses + 1

print('\nThanks for playing the Wheel of Fortune!')
