import os
from art import logo

clear = lambda: os.system('clear')

# Add
def add(n1, n2):
  return n1 + n2

# Substract
def substract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": substract,
  '*': multiply,
  '/': divide,
}


def calculator():
  print(logo)
  
  continue_calculation = True
  num1 = float(input("What's the first number: "))
  for operation in operations:
    print(operation)
  
  while continue_calculation:  
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number: "))
    func = operations[operation_symbol]
    answer = func(num1, num2)
  
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    prompt = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation.: ")
    if prompt == 'y':
      num1 = answer
    else:
      continue_calculation = False
      clear()
      calculator()
      
calculator()
