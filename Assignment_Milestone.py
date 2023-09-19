secret_word = "nephi"

print("your hint is: ", end="") 
for letter in secret_word:
    print("_ ", end="")
print()

guess = input("what is your guess: ")
guess_count = 1

while guess != secret_word:
    guess_length = len(guess)
    for i in range(guess_length):
     letter = guess[i]
    if letter == secret_word[1]:
       print(letter.upper())
    elif letter in secret_word:
       print(letter.lower())

       print("Sorry, the guess must have the same number of letters as the secret word.")
       guess = input("what is your guess: ")
       guess_count += 1

       print(f"you guessed it in {guess_count} guesses!!!")