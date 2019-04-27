from money_tracker import MoneyTracker
from parse_money_tracker_data import Parser
from money_tracker_menu import print_menu, get_input


def main():
    print("Hello!")
    parser = Parser()
    parsed_content = parser.parse_file('money_tracker.txt')
    mt = MoneyTracker(parsed_content)
    mt.create_database()
    while True:
        choice = get_input()
        if choice == 1:
            print(mt)
        elif choice == 2:
            mt.print_records_in_date(parser.get_date())
        elif choice == 3:
            mt.print_records_in_category_ordered_by_labels('expense')
        elif choice == 4:
            amount = parser.get_amount()
            date = parser.get_date()
            label = input('label: ')
            mt.add_record(date, amount, label, 'income')
        elif choice == 5:
            amount = parser.get_amount()
            date = parser.get_date()
            label = input('label: ')
            mt.add_record(date, amount, label, 'expense')
        elif choice == 6:
            break
        elif choice == -1:
            continue


if __name__ == '__main__':
    main()
