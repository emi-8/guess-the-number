import random

def computer_guess(x):
    high = x
    low = 1
    feedback = ''
    
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = (input(f'Is the number {guess} too high (H), too low (L) or correct (C)?')).lower()
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1
    
    print(f'The computer guessed your number {guess}!')   



computer_guess(100)