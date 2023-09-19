print("welcome to the guess word game")

secret_word = "console"
guess =""
guess_count = 0
guess_limit = 4
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
            print("out of guesses, YOU LOSE!")
else:
    print("you win!") 

    
       
