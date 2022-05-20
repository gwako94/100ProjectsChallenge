import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]


user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors:\n'))


if user_choice > 2:
  print("You typed in an invalid number. You lose!")
  
else:
  print(f"{choices[user_choice]}")
  computer_choice = random.randint(0,2)
  print(f"Computer Chose: \n{choices[user_choice]}\n")

  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  
  elif user_choice == 2 and computer_choice == 0: 
    print("You lose!")
    
  elif user_choice > computer_choice:
    print("You win!")
    
  elif user_choice < computer_choice:
    print("You lose!")
    
  elif user_choice == computer_choice:
    print("It's a draw!")
    