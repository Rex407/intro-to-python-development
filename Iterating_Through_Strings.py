
secret_word = "commitment"
favorite_word = input("what is your favorite word?: ").lower()
for i in range(len(secret_word)):
    word = secret_word[i]
    if favorite_word in word:
        print("_", end= "")
    else:
        print(word.lower(), end="")
print()        