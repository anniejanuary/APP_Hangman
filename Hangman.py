import random

# using the 'word_list' from hangman_words.py
import hangman_words
chosen_word = random.choice(hangman_words.word_list)

#🔎Testing code
#print(f'Pssst, the solution is {chosen_word}.')

# setting number of lives = 6 (6 stages of gallows)
lives = 6

#Importing the logo from hangman_art.py
import hangman_ASCII_art
print(hangman_ASCII_art.logo)

# turning str chosen_word into an appended list
chosen_word_list = []
for letter in chosen_word:
  chosen_word_list.append(letter)

# creating blanks
display = []
for letter in chosen_word:
  display.append("_")    #🔀 display += "_"

end_of_game = False

guessed_letters = []

# while loop for guessing letters
while not end_of_game:  #🔀 while end_of_game == False:
  guess = input("Guess a letter: ").lower()

  guessed_letters += guess
  #If the user has entered a letter they've already guessed, print the letter and let them know
  if guess not in display:
      
    # checking if guessed letter in chosen_word_list or not:
    #❎i = 0  -> not necessary, len(display) range starts at 0 anyway:
    for i in range(len(display)):
        if chosen_word_list[i] == guess:
          display[i] = guess
          #❎i += 1   ->  not necessary, FOR LOOP loops w/o it
  else:
    print("You've already guessed this letter, try another one: ")
        
  # missed letters: deducting lives and drawing gallow stages 
  if guess not in chosen_word_list:
    # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    lives -= 1    
    print(hangman_ASCII_art.stages[lives])
    print(f"Letter '{guess}' is not in the word")

    # when all lives are lost
    if lives == 0:
      end_of_game = True
      print("You lose!")
      print(f"The word was: '{chosen_word}'")
      
  # turnning guessed letters display list into a str w/o commas
  print(' '.join(display))
  print(f"Used letters: {guessed_letters}")
  
  # when all letters are guessed correctly
  if "_" not in display:
      end_of_game = True
      print("You win!")
