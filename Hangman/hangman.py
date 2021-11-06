import random
from hangman_art import stages, logo
from words import word_list
import os

print(logo)

gameMode = False
lives = 6
chosenWord = random.choice(word_list)

display = []
for _ in range(len(chosenWord)):
  display += '_'

print(chosenWord)

while not gameMode:
  guess = input('Guess a letter: ').lower()

  os.system('cls')

  for position in range(len(chosenWord)):
    letter = chosenWord[position]
    if letter == guess:
      display[position] = letter

  print(f"{(' ').join(display)}")
  
  if guess not in chosenWord:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      gameMode = True
      print('You Lose')
      
  if '_' not in display:
    gameMode = True
    print('You Win The Challenge')

  print(stages[lives])
