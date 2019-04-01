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
            print("\nError, provided value not in range form 1 to 6!\nPlease try again\n")
            return -1
    return choice


def main():
    print("Hello!")
    content = read_data()
    all_user_data = build_user_data(content)
    while True:
        choice = get_input()
        if choice == 1:
            list_user_data(all_user_data)
        elif choice == 2:
            date = get_date()
            print_user_data_per_date(date, all_user_data)
        elif choice == 3:
            print_user_expenses_ordered_by_categories(all_user_data)
        elif choice == 4:
            amount, label, date = get_income_or_expense('income')
            add_income(label, amount, date, all_user_data)
        elif choice == 5:
            amount, label, date = get_income_or_expense('expense')
            add_expense(label, amount, date, all_user_data)
        elif choice == 6:
            break
        elif choice == -1:
            continue