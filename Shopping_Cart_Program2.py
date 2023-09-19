foods = []
princes = []
total = [] 





def mainMenu():
    while True:


        # Display the main menu
        print('''
        Welcome to the Shopping Cart Program!

        Please select one of the following:

        1. Add item
        2. View cart
        3. Remove item
        4. Compute total
        5. Quit
        ''')

        selection = input("Please enter an action: ")



        if selection == "1":
            addItem()
        elif selection == "2":
            displayList()
        elif selection == "3":
            removeItem()
        elif selection == "4":
            computeTotal()
        elif selection == "5":
            pass
        else:
            print("you did not make a valid selection.")

shopping_list = ["oranges", "bananas", "apples" "potatoes"]
prince_list = ["3.49", "2.50", " 4.00"]

def addItem():
    item = input("What item would you like to add?: ")
    shopping_list.append(item)
    prince_list.append(item)
    item = input(f"What is the price of: {item} ")
    print(item +' '+ "has been added to the cart.")
    print(f"{item} has been added to the cart.")

def displayList():
    print()
    print("The contents of the shopping cart are:")
    for i in  shopping_list(5):
        print("0 " + i)

def removeItem():
    item = input("Which item would you like to remove?: ")
    cart=['item 1','item2','item3']
    item_to_remove='item2'
    del cart[cart.index(item_to_remove)]
    print(cart)

def computetotal():
    total = 0
    for item in list.items.price:
        total+=item.price
        return total
    

mainMenu()
