#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

answer = random.randint(1, 100)
EASY_LEVEL = 10
HARD_LEVEL = 5


def set_difficulty():
    prompt = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if prompt == 'easy':
        return EASY_LEVEL
    elif prompt == 'hard':
        return HARD_LEVEL
    else: 
        print("Invalid Diffuculty Level")
        return set_difficulty()

def check_answer(guess, answer):

  if guess > answer:
    print("Too high!")

  elif guess < answer:
    print("Too low")

  else:
    print(f"You got it! The answer was {answer}")

  
def game():

    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)

    attempts_remaining = set_difficulty()

    guess = 0
    while attempts_remaining:
        print(f"You have {attempts_remaining} attempts remaining to guess the number.")
        guess = int(input("make a guess: "))

        check_answer(guess, answer)

        if guess != answer and attempts_remaining != 1: print("Guess again")

        attempts_remaining -= 1

    if attempts_remaining == 0: print(f"You've run out of guesses, you lose. The answer was {answer}")

game()