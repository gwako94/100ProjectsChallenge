############### Blackjack Project #####################
import os
import random
from art import logo

clear = lambda: os.system('clear')

def deal_card():
  """ Return a random card from the deck """
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

  
# Calculate hand
def calculate_hand(cards):
  total_hand = sum(cards)
  if total_hand == 21 and len(cards) ==  2:
    return 0

  if total_hand > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
    
  return total_hand


def compare(user_total, computer_total):
  if user_total == computer_total:
    return  "It's a draw!"
    
  elif computer_total == 0:
    return "You Lose, opponent has blackjack!"
    
  elif user_total == 0:
    return "You win, it's a blackjack!"

  elif user_total > 21:
    return "You Lose, it's a bust!"

  elif computer_total > 21:
    return "You win, opponent has a bust!"

  elif user_total  > computer_total:
    return "You win!"
    
  else:
    return "You lose!"
    

def play_game():
    
  print(logo)

  is_game_over = False
  
  # Deal the user and computer 2 cards using deal_card()
  user_cards = [deal_card() for _ in range(2)]
  computer_cards = [deal_card() for _ in range(2)]
  
  while not is_game_over:
    user_score = calculate_hand(user_cards)
    computer_score = calculate_hand(computer_cards)
    
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_hand(computer_cards)
  
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's fnal hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
