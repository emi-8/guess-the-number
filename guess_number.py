import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {10}: '))
        if guess > random_number:
            print('Too high. Guess again.')
        else:
            print('Too low. Guess again.')

    print(f'You guessed the correct number {random_number}! Congrats!')


guess(10)
