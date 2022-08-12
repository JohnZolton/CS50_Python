import random

while True:
    try:
        level = input('Level: ')
        if int(level) > 0:
            break
    except ValueError:
        continue

level = int(level)
answer = random.randrange(0, level)

while True:
    guess = input('Guess: ')
    try:
        if int(guess) >0 and int(guess) <= level:
            guess = int(guess)

            if guess == answer:
                print('Just right!')
                break
            elif guess > answer:
                print('Too large!')
            elif guess < answer:
                print('Too small!')
    except ValueError:
        continue