word_list = ["aardvark", "baboon", "camel"]

import random

gallows_stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


chosen_word = random.choice(word_list)
#🔎Testing code
print(f'Pssst, the solution is {chosen_word}.')

# setting number of lives = 6 (6 stages of gallows)
lives = 6

# turning str chosen_word into an appended list
chosen_word_list = []
for letter in chosen_word:
  chosen_word_list.append(letter)

# creating blanks
display = []
for letter in chosen_word:
  display.append("_")    #🔀 display += "_"

end_of_game = False

# while loop for guessing letters
while not end_of_game:  #🔀 while end_of_game == False:
  guess = input("Guess a letter: ").lower()
  
  # checking if guessed letter in chosen_word_list or not:
  #❎i = 0  -> not necessary, len(display) range starts at 0 anyway:
  for i in range(len(display)):
      if chosen_word_list[i] == guess:
        display[i] = guess
        #❎i += 1   ->  not necessary, FOR LOOP loops w/o it
        
  # missed letters: deducting lives and drawing gallow stages 
  if guess not in chosen_word_list:
    lives -= 1    
    print(gallows_stages[lives])

    # when all lives are lost
    if lives == 0:
      end_of_game = True
      print("You lose!")
      
  # removing commas from guessed letters display list 
  print(' '.join(display))
  
  # when all letters are guessed correctly
  if "_" not in display:
      end_of_game = True
      print("You win!")
