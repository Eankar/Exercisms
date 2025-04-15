"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        if current_cart.get(item):
            current_cart[item] = current_cart[item] + 1
        else:
            current_cart[item] = 1
    
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return dict.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas |= recipe_updates
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    #print(cart)
    #print(aisle_mapping)
    #print(cart.update(aisle_mapping))
    #print(sorted(cart.update(aisle_mapping), reverse=True))
    #return cart.update(aisle_mapping)
    for i in cart:
        cart[i] = [cart[i], aisle_mapping[i][0], aisle_mapping[i][1]]
        #print(cart[i])
    #print(cart)
    #print(sorted(cart.items(), reverse=True))
    return sorted(cart.items(), reverse=True)


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for item, ordered_quantity in fulfillment_cart.items():
        store_inventory[item][0] -= ordered_quantity

    for item, stock_info in store_inventory.items():
        if stock_info[0] <= 0:
            store_inventory[item][0] = "Out of Stock"

    return store_inventory


#add_item({"Apple": 1, "Banana": 4}, ("Apple", "Banana", "Orange"))
# send_to_store({"Banana": 3, "Apple": 2, "Orange": 1, "Milk": 2},
# {
#             "Banana": ["Aisle 5", False],
#             "Apple": ["Aisle 4", False],
#             "Orange": ["Aisle 4", False],
#             "Milk": ["Aisle 2", True],
#         })