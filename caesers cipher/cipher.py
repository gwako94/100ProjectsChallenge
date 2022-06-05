import string
from art import logo

alphabet = string.ascii_lowercase

def caeser_cipher(start_text, shift_number, cipher_direction):
  message = ''

  if cipher_direction == 'decode':
      shift_number = shift_number * -1

  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      position += shift_number
      if position > 25:
          position -= 26
      elif position < 0:
          position += 26
      message += alphabet[position]

    else:
      message += char
      
  print(f"Here is the {cipher_direction}d text: {message}")

should_continue = True

while should_continue:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caeser_cipher(start_text=text, shift_number=shift, cipher_direction=direction)

  prompt = input("Type 'yes' if you want to go again, otherwise 'no'.\n")

  if prompt == 'no':
    should_continue = False
    print("Goodbye")
