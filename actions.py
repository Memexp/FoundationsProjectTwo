# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "The Shopping Fond"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    print ("Our stores: ")
    for store in stores:
        print (store.name)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    for store in stores:
        if store_name == store.name.lower():
            return store
   
    return False    

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    print_stores()
    print ("Pick a store by typing its name. Or type 'checkout' to pay your bills and say your goodbyes.")

    while True:
        userinput = input().lower()
        if userinput == "checkout":
            return False
        elif get_store(userinput):
            return get_store(userinput)
        else:
            print ("No store with that name. Please try again.")



def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    flag = False
    picked_store.print_products()

    print ("Enter the products that you want: ")
    while True:
        user_input= input().lower()
        if user_input == "back":
            break
        
        for product in picked_store.products:
            if product.name.lower() == user_input:
                cart.add_to_cart(product)
                flag =  True

        if flag == False:
            print ("You entered an invalid product name.")

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    
    while True:
        store = pick_store()
        if store:
            pick_products(cart, store)
        else:
            break
    cart.checkout()            

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
