import random
 
name = input("What is your guess? ")
 
 

print("Good Luck ! ", name)
 

words = ['church']
 

word = random.choice(words)
 
 

print("Your hint is: _ _ _ _ _ _")
 

guesses = ''
 
turns = 6
 
while turns > 0:
 
    failed = 0
 
    for char in word:
 

        if char in guesses:

            print(char, end=" ")
 

        else:

            print("_")
 

            failed += 1
 

    if failed == 0:


        print("Congratulations!")
 
        print("The word is: ", word)

        break
 
    print()

    guess = input("Sorry, the guess must have the same number of letters as the secret word.:")
 
    guesses += guess
 
    if guess not in word:
 

        turns -= 1
 

    

        print("Wrong")
 


        print("You have", + turns, 'more guesses')
 

        if turns == 0:

            print("You Loose")