
print("Welcome to the Shopping Cart Program!")
print()

cartitems = []
cartTotal = []
cartprice = []

menu_options = (f'1. Add item' '2. View cart' '3. Remove item' '4. Compute total' '5. Quit')

while True:
    print()
    print('Please select one of the following:')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')

    print()
    user_input = input('Please enter an action: ')

    def additem():
       print() 
       print(f"Adding {user_input} to your shopping list.")
       cartitems.append(user_input)
       def viewcart():
           if len(cartitems)>0:
               for i in range(len(cartitems)):
                   print(f"{i+1}. {cartitems[i]}")
                   print()
                   else:
print("Your shopping cart is empty.")
def removeitem():
    if len(cartitems)>0:
        print()
        print(f"Removing {user_input} from your shopping list.")
        del cartitems[int(user_input))-1]
print()
