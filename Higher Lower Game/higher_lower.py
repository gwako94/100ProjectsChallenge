import os
import random
from art import logo, vs
from game_data import data

clear = lambda: os.system("clear")


def get_random_account():
    """Get a random accout"""
    return random.choice(data)

def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account['name']
    description = account['description']
    country = account['country']
    return  f"{name}, a {description}, from {country}."

def check_answer(guess, a_followers, b_folowers):
    if a_followers > b_folowers:
        return guess == 'a'
    else:
        return guess == 'b'


def game():

    print(logo)
    game_over = False
    score = 0
    account_b = get_random_account()

    while not game_over:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ")
        a_followers = account_a['follower_count']
        b_followers = account_b['follower_count']
        is_correct = check_answer(guess, a_followers, b_followers)

        clear()
        print(logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_over = True
            print(f"Sorry, that's wrong. Final score: {score}")
game()