word_list = ["aardvark", "baboon", "camel"]

import random

chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("Guess a letter: ").lower()

#      Way 1
for x in chosen_word:
  if x == guess:
    print("True")
  else:
    print("False")


#      Way 2
#i = 0
#for i in range(len(chosen_word)):
#  if guess in chosen_word[i]:
#    print("True")
#    i += 1
#  else:
#    print("False")
#    i += 1
  
    

