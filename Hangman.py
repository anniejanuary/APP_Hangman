word_list = ["aardvark", "baboon", "camel"]

import random

chosen_word = random.choice(word_list)
🔎#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

chosen_word_list = []
for letter in chosen_word:
  chosen_word_list.append(letter)

display = []
for letter in chosen_word:
  display.append("_")    🔀# display += "_"

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

end_of_game = False

while not end_of_game:  🔀# while end_of_game == False:
  guess = input("Guess a letter: ").lower()
     
  ❎#i = 0  -> not necessary, len(display) range starts at 0 anyway:
  for i in range(len(display)):
      if chosen_word_list[i] == guess:
        display[i] = guess
        ❎#i += 1   ->  not necessary, FOR LOOP loops w/o it

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

  print(display)
  
  if "_" not in display:
      end_of_game = True
      print("You've won!")
