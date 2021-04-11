#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
print('''
  
   _____ _    _ ______  _____ _____                   _   _ _    _ __  __ ____  ______ _____  
  / ____| |  | |  ____|/ ____/ ____|        /\       | \ | | |  | |  \/  |  _ \|  ____|  __ \ 
 | |  __| |  | | |__  | (___| (___         /  \      |  \| | |  | | \  / | |_) | |__  | |__) |
 | | |_ | |  | |  __|  \___ \\___ \       / /\ \     | . ` | |  | | |\/| |  _ <|  __| |  _  / 
 | |__| | |__| | |____ ____) |___) |     / ____ \    | |\  | |__| | |  | | |_) | |____| | \ \ 
  \_____|\____/|______|_____/_____/     /_/    \_\   |_| \_|\____/|_|  |_|____/|______|_|  \_\
                                                                                              
  ''')
print("Welcome to Number Guessing Game!\n I'm thinking of a number between 1 to 100")
difficulty = input("Choose difficulty level: Easy or Hard => ").lower()
attempts = 0
if difficulty == "easy":
  attempts = 10
else:
  attempts = 5

should_find = random.randint(1, 101)

for key in range(attempts):
  guess = int(input(f"You have {attempts} to guess a number. \n Make a guess: "))
  if guess > should_find:
    print("Too High")
    attempts-=1
    if attempts == 0:
      print(f"No more attempts left\n YOU LOSS")
  elif guess < should_find:
    print("Too Low")
    attempts-=1
    if attempts == 0:
      print(f"No more attempts left\n YOU LOSS")
  elif guess == should_find:
    print("You WIN")
    quit()