"""
File: hangman.py
Name: 黃科諺
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Input: str, ask users to enter an alphabet as his or her guess
    Output: str, show whether the guess is correct, the updated dashed lines, and the guesses left
    """
    ans=random_word()
    print('The word looks like: ', end='')
    for i in range(len(ans)):
        print('-', end='')
    print('')
    guess = N_TURNS
    print('You have '+str(N_TURNS)+' guesses left.')
    response = ''
    for i in range(len(ans)):
        response+='-'
    while True:
        alphabet=input('Your guess: ')
        alphabet=alphabet.upper()
        if not alphabet.isalpha():
            print('illegal format.')
        elif len(alphabet)!=1:
            print('illegal format.')
        elif alphabet in ans:
            print('You are correct!')
            for i in range(len(ans)):
                ch = ans[i]
                ch_response = response[i]
                if alphabet == ch:
                    response += alphabet
                elif ch_response.isalpha():
                    response += ch_response
                else:
                    response += '-'
            response = response[len(ans):]
            if response == ans:
                print('You win!!')
                print('The word was: ' + ans)
                break
            else:
                print('The word looks like: ' + response)
                print('You have ' + str(guess) + ' guesses left.')
        else:
            print('There is no ' + alphabet + '\'s ' + 'in the word.')
            guess -= 1
            if guess == 0:
                print('You are completely hung : (')
                print('The word was: ' + ans)
                break
            else:
                print('The word looks like: ' + response)
                print('You have ' + str(guess) + ' guesses left.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
