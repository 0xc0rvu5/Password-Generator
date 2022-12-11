import string, random


#initialize lists
PASSWORD_LIST = []
LETTERS = []
NUMBERS = []
SYMBOLS = []
#initialize variables with all alpha/symbol possibilites
PRE_LETTERS = string.ascii_lowercase + string.ascii_uppercase
PRE_SYMBOLS = string.punctuation


#convert strings to supplied lists
for letter in PRE_LETTERS:
    LETTERS.append(letter)

for symbol in PRE_SYMBOLS:
    SYMBOLS.append(symbol)

for number in range(10):
    NUMBERS.append(str(number))


print("Welcome to the PyPassword Generator!")
#query user
Q_LETTERS = int(input("How many letters would you like in your password?\n")) 
Q_SYMBOLS = int(input(f"How many symbols would you like?\n"))
Q_NUMBERS = int(input(f"How many numbers would you like?\n"))


#randomization
for char in range(1, Q_LETTERS + 1):
    PASSWORD_LIST += random.choice(LETTERS)

for char in range(1, Q_SYMBOLS + 1):
    PASSWORD_LIST += random.choice(SYMBOLS)

for char in range(1, Q_NUMBERS + 1):
    PASSWORD_LIST += random.choice(NUMBERS)

random.shuffle(PASSWORD_LIST)

#final result printed
PASSWORD = ''
for char in PASSWORD_LIST:
    PASSWORD += char
print(f'Your password will be: {PASSWORD}')