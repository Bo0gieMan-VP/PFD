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
    if item in g_dict.keys():
        g_dict[item] += 1
    else:
        g_dict[item] = 1

def remove_item(item, g_dict):
    if item in g_dict.keys():
        if g_dict[item] > 1:
            g_dict[item] -= 1
        else:
            del g_dict[item]
        return True
    else:
        return False

def build_dict(alist):
    new_dict = {}
    for item in alist:
        if item.title().strip() in new_dict.keys():
            new_dict[item.title().strip()] += 1
        else:
            new_dict[item.title().strip()] = 1
    return new_dict

def sort_dict(adict):
    keys = sorted(list(adict.keys()))
    new_dict = {}
    for key in keys:
        new_dict[key] = adict[key]
    return new_dict

def total_delete(item, adict):
    if item in adict.keys():
        del adict[item]
        return True
    else:
        return False

def total_sum(glist):
    sum = 0
    for item in glist:
        sum += glist[item]
    return sum

def main():
    user_str = input("Enter a grocery list with commas: ")
    grocery_list = user_str.split(",") if len(user_str) > 0 else []
    grocery_list = build_dict(grocery_list)
    while True:
        choice = input(
    f"""{colored("[SHOW]",'blue')} Show Grocery List
{colored("[TOTAL]",'blue')} How many items in the list?
{colored("[FIND]",'blue')} Check if an item is on the list
{colored("[COUNT]",'blue')} How many times a item appears
{colored("[DEL]",'blue')} Delete an item from the list
{colored("[ADD]",'blue')} Add an item to the list
{colored("[SORT]",'blue')} Sort list alphabetically
{colored("[SHOW-ILL]",'blue')} Show all illegal items
{colored("[TOTAL-DEL]",'blue')} Remove item completely
{colored("[SHOW-POP]",'blue')} Show items by popularity
{colored("[TOTAL-SUM]",'blue')} Show the ammount of products
{colored("[EXIT]",'blue')} Exit program
                                                                        {colored("Enter a command:", 'red')} """).upper().strip()
        print(colored("--------------------------------------------------------------------------------------", 'yellow'))
        match choice:
            case "SHOW":
                show_list(grocery_list, True) if len(grocery_list.keys()) > 0 else print(colored("No items on the list", 'red'))
            case "TOTAL":
                print(len(grocery_list.keys()))
            case "FIND":
                item = input("Is that item on the list? ").title().strip()
                print(colored("Yes", "green") if item in grocery_list else colored("No", 'red'))
            case "COUNT":
                item = input("Which item to check? ").title().strip()
                print((grocery_list[item] , "Times") if item in grocery_list else colored(f"{item} not in the list", 'red'))
            case "DEL":
                item = input("Which item to remove? ").title().strip()
                print(colored(f"{item} deleted from the list", 'green') if remove_item(item, grocery_list) else colored(f"{item} not on the list", 'red'))
            case "ADD":
                item = input("What would you like to add to the list? ").title().strip()
                add_item(item, grocery_list)
            case "SORT":
                grocery_list = sort_dict(grocery_list)
                print(colored("List sorted", 'green'))
            case "SHOW-ILL":
                print(get_invalid_items(grocery_list) if len(get_invalid_items(grocery_list)) > 0 else colored("None", 'green'))
            case "TOTAL-DEL":
                item = input("Which item to remove? ").title().strip()
                print(colored("Removed all of "+item.title(), 'green') if total_delete(item, grocery_list) else f"{item} is not on the list")
            case "SHOW-POP":
                show_list(grocery_list, False)
            case "TOTAL-SUM":
                print(f"{total_sum(grocery_list)} items on the list" if total_sum(grocery_list) > 0 else colored("No items on the list!", 'red'))
            case "EXIT":
                break
            case _:
                print(colored("Unknown selection, select again", 'red'))
        print(colored("--------------------------------------------------------------------------------------", 'yellow'))

if __name__ == "__main__":
    main()