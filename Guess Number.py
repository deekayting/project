# This is a number guessing game
import random
print('Hello! How are you? What is your name?')
playerName = input()
print('Hello ' + playerName + ',I\'m guessing a number between 0 and 30. Can you guess what number it is? You have 6 chances.')

# Ask player to guess the number 6 times.
secretNumber = random.randint(0, 30)
print('Debug: the secret number is ' + str(secretNumber))
for guessTaken in range(1, 7):
    if (7 - guessTaken) == 1:
        print('Take your last guess.')
    else:
        print('Take a guess. You have ' + str(7 - guessTaken) + ' more chances')
    guessNumber = input()
    try:
        if int(guessNumber) < secretNumber:
            print('Your guess is too low.')
        elif int(guessNumber) > secretNumber:
            print('Your guess is too high.')
        else:
            break
    except ValueError:
        print('Please type your guess in numerical format e.g. 1, 2, 3, etc.')

if int(guessNumber) == secretNumber:   
    print('Good job! You guessed my number in ' + str(guessTaken) + ' tries!')

else:  
    print('You have used up your ' + str(guessTaken) + ' guesses. My number is actually ' + str(secretNumber) + '.')    
