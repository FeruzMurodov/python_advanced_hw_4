import random


def rock_paper_scissors():
    print('Start...')
    players_act = input('Type "1" for rock, "2" for paper, "3" for scissors: ')
    if players_act in ('1','2','3'):
        players_gun = 'rock' if players_act == '1' \
            else 'paper' if players_act == '2' \
            else 'scissors' if players_act == '3' \
            else print('Enter appropiate number!')
        print(f"You: {players_gun}")
        computers_act = random.choice([1, 2, 3])
        computers_gun = 'rock' if computers_act == 1 \
            else 'paper' if computers_act == 2 \
            else 'scissors'
        print(f"Computer: {computers_gun}")
        if players_gun == 'rock' and computers_gun == 'rock':
            print('Nobody won!')
        elif players_gun == 'rock' and computers_gun == 'paper':
            print('You lose!')
        elif players_gun == 'rock' and computers_gun == 'scissors':
            print('You won!')
        elif players_gun == 'paper' and computers_gun == 'paper':
            print('Nobody won!')
        elif players_gun == 'paper' and computers_gun == 'rock':
            print('You won!')
        elif players_gun == 'paper' and computers_gun == 'scissors':
            print('You lose!')
        elif players_gun == 'scissors' and computers_gun == 'scissors':
            print('Nobody won!')
        elif players_gun == 'scissors' and computers_gun == 'rock':
            print('You lose!')
        elif players_gun == 'scissors' and computers_gun == 'paper':
            print('You won!')
    else:
        print('Please type "1" for rock, "2" for paper, "3" for scissors: ')




def guess_the_number():
    number_comp = random.randrange(0, 10)
    print('Computer thought some number... Guess what number is it?')
    while True:
        number_player = int(input('Enter the number: '))
        if number_comp == number_player:
            print(f'You won! Number was truly {number_comp}!')
            mainMenu()
        else:
            print('No. ;-)')


def mainMenu():
    while True:
        command = input('Choose the game: \n'
                        'Enter "1" to play "Rock paper scissors"\n'
                        'Enter "2" to play "Guess the number": ')
        if command == '1':
            rock_paper_scissors()
        elif command == '2':
            guess_the_number()
        elif command == 'x':
            exit()
        else:
            print("You have entered incorrect symbol. Enter 'x' to quit game or")


mainMenu()
