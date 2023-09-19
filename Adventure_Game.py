answer = input("do you want to play this text adventure game? [yes/no] ")

if answer == "yes":

    print("thats great!")
    print()
    answer = input("You are walking through a dark forest and find two items: [match/flash light] ")
    if answer == "MATCH":
        print("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. ")
        print()
        answer = input("Do you want to RUN, or HIDE behind a tree? [run/hide]")

        if answer == "RUN":
            print("you run away! you win!")

        else:
            print("invalid option, you loose!")


