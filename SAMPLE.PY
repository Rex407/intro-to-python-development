def menu():
    print("[1] option 1")
    print("[2] option 2")
    print("[0] exit the program.")


    menu()
    option = int(input("Please select one of the following:"))

    while option != 0:
        if option == 1:
            #do option 1 stuff
            print("What item would you like to add?")
        elif option == 2:
            #do option 2 stuff
            print("The contents of the shopping cart are:")
        else:
            print("invalid option.")

            print()
            menu()
            option = int(input("Please enter an action:"))

            print("thanks for using this program. goodbye")