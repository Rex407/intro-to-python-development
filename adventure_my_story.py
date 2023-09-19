answer = input("do you want to play this text adveture game? [YES/NO] ")

if answer == "yes":

    print("that's great!")
    print()
    answer = input("do you want to explore a cave or jungle? [CAVE/JUNGLE]")

if answer == "CAVE":
    print("you go into the cave and see a sleeping bear")
    print()
    answer = input("do you want to fight or run? [FIGHT/RUN] ")

    if answer == "fight":
        print("bears are really strong! you lose")

    elif answer == "run":
        print("you ran away! you win!")

    else:
        print("invalid option, you lose!")
