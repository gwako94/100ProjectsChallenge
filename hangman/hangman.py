import random
from hangman_art import stages, logo
from hangman_wordlist import word_list 
import os

choosen_word = random.choice(word_list)
word_length = len(choosen_word)
end_of_game = False
lives = 6
display = ["_" for _ in range(word_length)]
clear = lambda: os.system('clear')

print(logo)


while not end_of_game:
  # Ask a user to guess a letter.
  guess = input("Guess a letter: ").lower()
  clear()

  if guess in display:
    print(f"You have already guessed {guess}")

  # check if guess is in choosen_word
  for i in range(word_length):
    if choosen_word[i] == guess:
      display[i] = guess

  # check if guess in choosen word
  if guess not in choosen_word:
    print(f"You guessed letter {guess}, that is not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose")

  print(" ".join(display))
  
  if '_' not in display:
    end_of_game = True
    print("You win")

  print(stages[lives])

print(choosen_word)
