# internal
import functions
import get_push

# standard
import os
import time
import sys

# colorama
from colorama import Fore

def Introduction():
    if sys.platform == 'linux':
        os.system('clear')
    else:
        os.system('cls')
    print(Fore.YELLOW + """
    +-------------------------------------------------------------------------+
    |                               Blog Helper                               |
    |                                                                         |
    |    This tool help you to managment your blog. with this, you can:       |
    |       [+] Show all ID and Title and you can choice wich you want to see |
    |       [+] Insert Title, Descriptin, and Category_id to post table       |
    |       [+] Insert category's name to Category table                      |
    |       [+] Show all category in a Category table                         |
    |       [+] And many other things...                                      |
    |                                                                         |
    |   Enjoy :))                                                             |
    +-------------------------------------------------------------------------+
    """)
    time.sleep(3)
    if sys.platform == 'linux':
        os.system('clear')
    else:
        os.system('cls')
    print(Fore.GREEN + "\nWhat you want? (please enter the number of which you want)")
    time.sleep(0.2)
    print(Fore.CYAN + f"""
        1: Insert your data such as title, description and category's ID to post table
        2: Insert name of category to category table
        3: Show ID and Title of you Blog
        4: Show all category you added

        {Fore.WHITE }If you want to clear the terminal, please press <c> button
        {Fore.WHITE }If you want to read list of tool, please press{Fore.GREEN} <l> {Fore.WHITE}button
        {Fore.WHITE }and if you want to exit, please press{Fore.RED} <e> {Fore.WHITE}button
    """)

def list_of_do():
    print(Fore.CYAN + f"""
        1: Insert your data such as title, description and category's ID to post table
        2: Insert name of category to category table
        3: Show ID and Title of you Blog
        4: Show all category you added

        {Fore.WHITE }If you want to clear the terminal, please press <c> button
        {Fore.WHITE }If you want to read list of tool, please press{Fore.GREEN} <l> {Fore.WHITE}button
        {Fore.WHITE }and if you want to exit, please press{Fore.RED} <e> {Fore.WHITE}button
    """)

def backend_and_user_interface():
    '''This function is id_title function from get_push and user connector'''
    while True:
        user_input = functions.binput()
        try:
            user_input = int(user_input)
        except:
            pass
        if isinstance(user_input, int):
            if user_input > 4:
                print(Fore.RED,'[-] your number is too high. please enter a number between 1,4',Fore.WHITE)
                continue
            elif user_input == 1:
                _id_title_connector()
            elif user_input == 2:
                _category_connector()
            elif user_input == 3:
                _post_title()
            elif user_input == 4:
                _categories()
        elif user_input == 'c':
            if sys.platform == 'linux':
                os.system('clear')
            else:
                os.system('cls')
        elif user_input == 'l':
            list_of_do()
        elif user_input == 'e':
            exit()
        elif len(user_input) == 0:
            continue

        else:
            print(Fore.RED, '[-] please enter a number not string or flout',Fore.WHITE)
            continue

def exit():
    while True:
        result = str(input(Fore.RED+'Do you really want to exit?([y],n) '+Fore.WHITE))
        if len(result) == 0 or result == 'y':
            sys.exit()
        elif result == 'n':
            break

def _id_title_connector():
    while True:
        checker = True
        title = str(input('please added your title: '))
        description = str(input('please added your description: '))
        try:
            id_category = int(input('please enter a number of category which you want: '))
        except ValueError:
            print(Fore.RED, '[-] please enter a number not string or flout or None',Fore.WHITE)
            checker = False
        if len(title) == 0:
            print(Fore.RED, '[-] title is empty. you can\'t set that as none ',Fore.WHITE)
            continue
        
        try:
            if checker:
                get_push.insert_post(title, description, id_category)
                print(Fore.GREEN,'[+] successfully added your post', Fore.WHITE)
                break
        except:
            print(Fore.RED, '[-] something went wrong! please try again',Fore.WHITE)

def _category_connector():
    while True:
        checker = False
        name = str(input('please added your category: '))
        try:
            expected_false = int(name)
        except:
            checker = True
        if checker and not len(name) == 0:
            get_push.insert_category(name)
            print(Fore.GREEN,'[+] successfully added your category',Fore.WHITE)
            break
        else:
            print(Fore.RED,'[-] you can\'t enter number or None',Fore.WHITE)

def _post_title():
    datas = get_push.id_and_title()
    for data in datas:
        print(Fore.GREEN+data+Fore.WHITE)
    time.sleep(1.5)
    get_push.get_description()
def _categories():
    datas = get_push.categories()
    for data in datas:
        print(Fore.GREEN+data+Fore.WHITE)




if __name__ == '__main__':
    Introduction()
    backend_and_user_interface()
