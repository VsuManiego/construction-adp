# File:                     G402 - 90% Project Completion
# Authors:                  Angel Iana B. Acol
#                           Emman Patrick C. Durante
#                           Jay Em A. Paton-og
import fileinput


def menu_display():
    print('\n=============================================')
    print(' Directory for Construction Tools and Data ')
    print('=============================================')
    print('(1) Add New Tool to Directory')
    print('(2) Remove Tool from Directory')
    print('(3) Search Tool in Directory')
    print('(4) Print Directory Report')
    print('(99) Quit')
    choice = int(input("Enter choice: "))
    menu_selection(choice)


def menu_selection(choice):
    if choice == 1:
        add_directory()
    elif choice == 2:
        remove_directory()
    elif choice == 3:
        search_directory()
    elif choice == 4:
        print_directory()
    elif choice == 99:
        exit()


def add_directory():
    directory_file = open('Directory.txt', 'a')
    print('\033[1m' + "\nAdd Tool to the Directory" + '\033[0m')
    print("==========================")
    item_name = input("Enter the name of the tool: ")
    item_quantity = input(f"How many {item_name} are there: ")
    item_cost = input(f"How much does {item_name} cost (each) in Php: ")
    directory_file.write(item_name + '\n')
    directory_file.write(item_quantity + '\n')
    directory_file.write(item_cost + '\n')
    directory_file.close()
    print("\nSuccess! The tool has been added to the directory.")
    choice = int(input('Enter 98 to continue or 99 to exit: '))
    if choice == 98:
        menu_display()
    else:
        exit()


def remove_directory():
    print('\033[1m' + "\nRemoving Tool from Directory" + '\033[0m')
    print("============================")
    item_name = input("Enter the tool name to remove from directory: ")

    file = fileinput.input('Directory.txt', inplace=True)

    for line in file:
        if item_name in line:
            for i in range(2):
                next(file, None)
        else:
            print(line.strip('\n'), end='\n')
    print('\033[91m' + "The tool has been removed from the directory." + '\033[0m')
    choice = int(input('Enter 98 to continue or 99 to exit: '))
    if choice == 98:
        menu_display()
    else:
        exit()


def search_directory():
    print('\033[1m' + "\nSearching Directory" + '\033[0m')
    print('===================')
    item_name = input('Enter the name of the tool: ')
    f = open('Directory.txt', 'r')
    search = f.readlines()
    f.close()
    for i, line in enumerate(search):
        if item_name in line:
            for a in search[i:i + 1]:
                print('\n---------------\n'
                      'Tool: ', '\033[1m' + a + '\033[0m', end='')
            for b in search[i + 1:i + 2]:
                print('Quantity: ', '\033[1m' + b + '\033[0m', end='')
            for c in search[i + 2:i + 3]:
                print('Cost: ', '\033[1m' + c + '\033[0m', end='')
                print('---------------')
    choice = int(input('\nEnter 98 to continue or 99 to exit: '))
    if choice == 98:
        menu_display()
    else:
        exit()


def print_directory():
    directory_file = open('Directory.txt', 'r')
    item_name = directory_file.readline()
    print('\033[1m' + "\nCurrent Directory" + '\033[0m')
    print('-----------------')
    while item_name != '':
        item_quantity = directory_file.readline()
        item_cost = directory_file.readline()
        item_name = item_name.rstrip('\n')
        item_quantity = item_quantity.rstrip('\n')
        item_cost = item_cost.rstrip('\n')
        print('Tool: ', '\033[1m' + item_name + '\033[0m')
        print('Quantity: ', '\033[1m' + item_quantity + '\033[0m')
        print('Cost: ', '\033[1m' + item_cost + '\033[0m')
        print('-----------------')
        item_name = directory_file.readline()
    directory_file.close()

    choice = int(input('\nEnter 98 to continue or 99 to exit: '))
    if choice == 98:
        menu_display()
    else:
        exit()


menu_display()