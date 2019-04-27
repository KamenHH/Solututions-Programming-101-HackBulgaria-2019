def print_menu():
    print("""\nChoose one of the following options to continue:
1 - show all data
2 - show data for specific date
3 - show expenses, ordered by categories
4 - add new income
5 - add new expense
6 - exit\n""")


def get_input():
    print_menu()
    try:
        choice = int(input('Choice: '))
    except ValueError:
        print("\nError, provided value not a valid integer!\nPlease try again\n")
        return -1
    else:
        if choice < 1 or choice > 6:
            print("\nError, provided value not in range from 1 to 6!\nPlease try again\n")
            return -1
    return choice
