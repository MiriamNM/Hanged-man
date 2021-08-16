import random
import time

# Words list to hanged Man
dogs_names = ['dog', 'bat', 'horse', 'rabbit', 'camel', 'deer']
names = ['maria', 'mariana', 'miriam', 'mario', 'francisco', 'penelope', 'beatriz']

#Instructions
print('Welcome to the handed Man play')
time.sleep(2)
print('The game consists of finding the secret word letter by letter')
time.sleep(2)
print('You have only 5 lifes and you lose each one when you make a mistake.')
time.sleep(2)

print('Guess the word, put A if you want animal´s words or N if you what names of people')
time.sleep(2)
select_cat = input('Put the letter you chose: ')

while True:
    if select_cat.lower() == 'a':
        print('You chose the animals')
        word_secret = random.choice(dogs_names)
        break
    elif select_cat.lower() == 'n':
        print('You chose names of people')
        word_secret = random.choice(dogs_names)
        break
    else:
        print('Please chose one letter')
        select_cat = input('Put the letter you chose: ')

#lifes and start of play
#lifes
lifes = 5
letter_guess_list = []

#Word without letters
print('_' * len(word_secret))

while True:
    while True:
        guess_letter = input('Guess the letter: ')
        if (len(guess_letter) !=1 and guess_letter.isnumeric()):
            print('That is not a letter, try again')
        else:
            if guess_letter.lower()in letter_guess_list:
                print('You already put that letter, try another')
            else:
                letter_guess_list.append(guess_letter)
                if guess_letter.lower() in word_secret:
                    print('Congratulations, you guessed the word')
                    break
                else:
                    lifes = lifes - 1
                    print('mistake, you lost a life')
                    print('You have ' + str(lifes) + 'lifes')
                    break
    
    if lifes == 0:
        print('You lost, the secret word is: ' + word_secret)
        break

    actual_state = ''

    missing_letter = 0
    for letter in word_secret:
        if letter in letter_guess_list:
            actual_state = actual_state + letter
        else: 
            actual_state = actual_state + '_'
            missing_letter = missing_letter -1

#Print word with some letters
print(actual_state)

if missing_letter == 0:
    print('Contratulations, you are winner :)')
    print('the secret word is: ' + word_secret)
    