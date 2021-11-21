from termcolor import colored

def get_invalid_items(g_list):
    """
    Finds the items with doesn't match the requirements
    (Less than 3 characters long or not all alphabetic)
    :param g_list: Grocery list
    :type g_list: list
    :return: String of the illegal words
    :rtype: str
    """
    invalid = ""
    for item in g_list.keys():
        if not item.isalpha() or len(item) < 3:
            invalid += item+"\n"
    return invalid

def show_list(g_list, numbered):
    """
    Prints the list with items counter
    :param g_list: Grocery list
    :type g_list: list
    """
    counter = 1
    for item, quantity in g_list.items():
        print(colored(f"{counter}. {item}" if numbered else f"{quantity}x {item}", 'blue'))
        counter += 1

def get_ascii_value(word):
    """
    Returns the ascii value of a word
    :param word: Desired word
    :type word: str
    :return: Ascii Value
    """
    sum = 0
    for c in word:
        sum += ord(c)
    return sum

def add_item(item, g_dict):
    """
    Adding a new item to the list or increasing an existing one
    :param item: Item to add
    :param g_dict: Grocery List
    :type item: str
    :type g_dict: dict
    :return: None
    """
    if item in g_dict.keys():
        g_dict[item] += 1
    else:
        g_dict[item] = 1

def remove_item(item, g_dict):
    """
    Decrease the ammount of an item
    or completely remove if reached 0
    :param item: Item to remove
    :param g_dict: Grocery List
    :type item: str
    :type g_dict: dict
    :return: True if succeed or False if item isn't on the list
    :rtype: bool
    """
    if item in g_dict.keys():
        if g_dict[item] > 1:
            g_dict[item] -= 1
        else:
            del g_dict[item]
        return True
    else:
        return False

def build_dict(alist):
    """
    Builds and returns a new dictionary
    after formating the keys to title
    and removing whitespaces
    :param alist: List of items
    :type alist: list
    :return: A new dictionary
    :rtype: dict
    """
    new_dict = {}
    for item in alist:
        if item.title().strip() in new_dict.keys():
            new_dict[item.title().strip()] += 1
        else:
            new_dict[item.title().strip()] = 1
    return new_dict

def sort_dict(adict):
    """
    Sorts the dictionary alphabetically based on keys
    :param adict: The Grocery List
    :type adict: dict
    :return: A sorted dictionary
    :rtype: dict
    """
    keys = sorted(list(adict.keys()))
    new_dict = {}
    for key in keys:
        new_dict[key] = adict[key]
    return new_dict

def total_delete(item, adict):
    """
    Removes an item completely from the list no matter it's quantity
    :param item: Item to remove
    :param adict: Grocery List
    :type item: str
    :type adict: dict
    :return: True or False whether succeed or not
    :rtype: bool
    """
    if item in adict.keys():
        del adict[item]
        return True
    else:
        return False

def total_sum(glist):
    """
    Sums all the quantities in the list
    :param glist: Grocery List
    :type glist: dict
    :return: The sum of all quantities in the list
    :rtype: int
    """
    sum = 0
    for item in glist:
        sum += glist[item]
    return sum

def products_startswith(glist, key):
    """
    Makes a string with all items starts with a 'key'
    :param glist: Grocery List
    :param key: Search key
    :type glist: dict
    :type key: str
    :return: String-list of all the item it found
    :rtype: str
    """
    products = ""
    for k in glist.keys():
        products += k +" x"+str(glist[k])+"\n" if k.lower().startswith(key.lower()) else ""
    return products

def products_endswith(glist, key):
    """
    Makes a string with all items ends with a 'key'
    :param glist: Grocery List
    :param key: Search key
    :type glist: dict
    :type key: str
    :return: String-list of all the item it found
    :rtype: str
    """
    products = ""
    for k in glist.keys():
        products += k +" x"+str(glist[k])+"\n" if k.lower().endswith(key.lower()) else ""
    return products

def products_contains(glist, key):
    """
    Makes a string with all items contains a 'key'
    :param glist: Grocery List
    :param key: Search key
    :type glist: dict
    :type key: str
    :return: String-list of all the item it found
    :rtype: str
    """
    products = ""
    for k in glist.keys():
        products += k +" x"+str(glist[k])+"\n" if key.lower() in k.lower() else ""
    return products

def search(glist, key):
    """
    Translates the key and sends the job to the correct function
    :param glist: Grocery List
    :param key: Search key
    :type glist: dict
    :type key: str
    :return: String-list of all the item it found
    :rtype: str
    """
    if len(glist.keys()) > 0:
        if (key.endswith('*') and not key.startswith("*")) or (not key.endswith("*") and not key.startswith("*")):
            return products_startswith(glist, key.replace("*", ""))
        elif key.startswith('*') and not key.endswith('*'):
            return products_endswith(glist, key.replace("*", ""))
        else:
            return products_contains(glist, key.replace("*", ''))
    return colored("Product not on the list", 'red')

def get_top_three(glist):
    """
    Recieves all clients' lists and create a top 3 dictionary
    of all of them
    :param glist: All users' Grocery List
    :type glist: dict
    :return: Dictionary of Top 3 items
    :rtype: dict
    """
    items = {}
    for list in glist.keys():
        for item, value in glist[list].items():
            if item in items:
                items[item] += value
            else:
                items[item] = value
    top_three = {}
    for i in range(3):
        new_item = max(items, key=lambda item: items[item])
        top_three[new_item] = items[new_item]
        del items[new_item]

    return top_three


def menu(grocery_list, user):
    """
    Manages the whole program and commands
    :param grocery_list: All of the users lists
    :param user: The current user
    :type grocery_list: dict
    :type user: str
    :return: True or False whether the program ends
    :rtype: bool
    """
    if user not in grocery_list.keys():
        user_str = input("Enter a list seperated by commas: ")
        grocery_list[user] = user_str.split(",") if len(user_str) > 0 else []
        grocery_list[user] = build_dict(grocery_list[user])
    while True:
        choice = input(
f"""{colored("[SHOW]", 'blue')} Show Grocery List
{colored("[TOTAL]", 'blue')} How many items in the list?
{colored("[FIND]", 'blue')} Check if an item is on the list
{colored("[COUNT]", 'blue')} How many times a item appears
{colored("[DEL]", 'blue')} Delete an item from the list
{colored("[ADD]", 'blue')} Add an item to the list
{colored("[SORT]", 'blue')} Sort list alphabetically
{colored("[SHOW-ILL]", 'blue')} Show all illegal items
{colored("[TOTAL-DEL]", 'blue')} Remove item completely
{colored("[SHOW-POP]", 'blue')} Show items by popularity
{colored("[TOTAL-SUM]", 'blue')} Show the ammount of products
{colored("[SEARCH]", 'blue')} Show the ammount of products
{colored("[LOGOUT]", 'blue')} Logout
{colored("[EXIT]", 'blue')} Exit program
                                                                {colored("Enter a command:", 'red')} """).upper().strip()
        print(
            colored("--------------------------------------------------------------------------------------", 'yellow'))
        match choice:
            case "SHOW":
                show_list(grocery_list[user], True) if len(grocery_list[user].keys()) > 0 else print(
                    colored("No items on the list", 'red'))
            case "TOTAL":
                print(len(grocery_list[user].keys()))
            case "FIND":
                item = input("Is that item on the list? ").title().strip()
                print(colored("Yes", "green") if item in grocery_list[user] else colored("No", 'red'))
            case "COUNT":
                item = input("Which item to check? ").title().strip()
                print((grocery_list[user][item], "Times") if item in grocery_list[user] else colored(f"{item} not in the list",
                                                                                         'red'))
            case "DEL":
                item = input("Which item to remove? ").title().strip()
                print(colored(f"{item} deleted from the list", 'green') if remove_item(item, grocery_list[user]) else colored(
                    f"{item} not on the list", 'red'))
            case "ADD":
                item = input("What would you like to add to the list? ").title().strip()
                add_item(item, grocery_list[user])
            case "SORT":
                grocery_list[user] = sort_dict(grocery_list[user])
                print(colored("List sorted", 'green'))
            case "SHOW-ILL":
                print(get_invalid_items(grocery_list[user]) if len(get_invalid_items(grocery_list[user])) > 0 else colored("None",
                                                                                                               'green'))
            case "TOTAL-DEL":
                item = input("Which item to remove? ").title().strip()
                print(colored("Removed all of " + item.title(), 'green') if total_delete(item,
                                                                                         grocery_list[user]) else f"{item} is not on the list")
            case "SHOW-POP":
                show_list(grocery_list[user], False)
            case "TOP3":
                show_list(get_top_three(grocery_list),True)
            case "TOTAL-SUM":
                print(f"{total_sum(grocery_list[user])} items on the list" if total_sum(grocery_list[user]) > 0 else colored(
                    "No items on the list!", 'red'))
            case "SEARCH":
                key = input("Enter a query: ")
                print(search(grocery_list[user], key) if len(search(grocery_list[user], key)) > 0 else colored("Product not on the list", 'red'))
            case "LOGOUT":
                return
            case "EXIT":
               return True
            case _:
                print(colored("Unknown selection, select again", 'red'))
        print(
            colored("--------------------------------------------------------------------------------------", 'yellow'))

def main():
    grocery_list = {}
    exit_program = False
    while not exit_program:
        user = input("Enter your username: ")
        exit_program = menu(grocery_list, user)


if __name__ == "__main__":
    main()