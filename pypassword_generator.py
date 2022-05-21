import random
import string

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_letters = random.sample(letters, nr_letters)
random_numbers = random.sample(numbers, nr_numbers)
random_symbols = random.sample(symbols, nr_symbols)

random_pass = random_letters + random_symbols + random_numbers
random.shuffle(random_pass)
password = "".join(random_pass)
print(password)
