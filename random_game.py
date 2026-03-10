#!/usr/bin/env python3

from random import randint


def roll_dice():
    return randint(1, 6)


def generate_target_number(lower_limit=17, upper_limit=29):
    return randint(lower_limit, upper_limit)


if __name__ == '__main__':
    target_number = generate_target_number()

    print(f'Target number: {target_number}')
    print()

    total = 0

    while True:

        this_roll = roll_dice()

        total += this_roll

        print(f'You rolled {this_roll}. Your total is {total}.')

        again = input('Would you like to roll again? (y/n): ')
        if again == 'n':
            break

    score = abs(total - target_number)

    if score <= 5:
        print(f'Your score is {score}.')
    else:
        print('You lost!')