#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
EASY = 10
HARD = 5

print(logo)
level = input("Choose a difficulty level: Easy (e) or Hard (h): ")
def set_difficulty(level):
  
  if level == 'e':
    return EASY
  
  if level == 'h':
    return HARD

def game():
  print("number range is 1 to 100")
  answer = random.randint(1,100)
  attempts = set_difficulty(level)
  while attempts != 0:
    guess = int(input("guess a number between: "))
    if guess == answer:
      print("Yay!! you guessed the right number.")
      break
    if guess < answer:
      print("Wrong guess. Too low")
    if guess > answer:
      print("Wrong guess. Too high")
    attempts -= 1
    if attempts == 0:
      print("Game Over! No more attempts.")

game()

    
  


