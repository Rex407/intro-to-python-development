quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

answer = "yes"
while answer != 'no' :
    number = int(input('p""lease enter a number: '))
    for 1, letter in enumerate(quote):
        letter = quote[i]
        if i % number == 0:
            print(letter.upper(), end= "")
        else:
            print(letter, end= "")
    print()
    answer = input("Would you like to enter another number? ")            
