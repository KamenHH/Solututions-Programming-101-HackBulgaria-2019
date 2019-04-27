from category import Expense, Income
from datetime import datetime
from parse_money_tracker_data import Parser


class MoneyTracker:
    def __init__(self, content):
        self.raw_content = content
        self.database = []

    def __str__(self):
        self.sort_database()
        last_date = self.database[0][0]
        string = last_date.strftime('=== %d-%m-%Y ===') + '\n'
        for row in self.database:
            curr_date = row[0]
            if curr_date != last_date:
                string += curr_date.strftime('=== %d-%m-%Y ===') + '\n'
                last_date = curr_date
            string += ', '.join([str(item) for item in row[1:]]) + '\n'
        return string

    def create_database(self):
        for line in self.raw_content:
            try:
                date = datetime.strptime(line, '=== %d-%m-%Y ===')
            except ValueError:
                amount, label, category = line.split(', ')
                cat_obj = Expense(amount, label) if category == 'New Expense' \
                    else Income(amount, label)
                self.database.append([date, cat_obj, cat_obj.CATEGORY_STR])

    def sort_database(self):
        # self.database = [self.database[0]] + sorted(self.database[1:], key=lambda row: row[0])
        self.database.sort(key=lambda row: row[0])

    def add_record(self, date_object, amount, label, category):
        if category.title() in Income.CATEGORY_STR:
            self.database.append([date_object, Income(amount, label), Income.CATEGORY_STR])
        elif category.title() in Expense.CATEGORY_STR:
            self.database.append([date_object, Expense(amount, label), Expense.CATEGORY_STR])

    def get_records_in_category(self, target_category):
        records = []
        for row in self.database:
            date, cat_obj, category = row
            if isinstance(cat_obj, Income if target_category == 'income' else Expense):
                records.append(cat_obj)
        return records

    def get_records_in_date(self, target_date):
        records = []
        for row in self.database:
            date, cat_obj, category = row
            if target_date == date:
                records.append((cat_obj, cat_obj.CATEGORY_STR))
        return records

    def print_records_in_date(self, date):
        records = self.get_records_in_date(date)
        if records:
            print(date.strftime('=== %d-%m-%Y ==='))
            for record in records:
                cat_obj, category = record
                print(cat_obj, category)

    def get_all_category_labels(self, target_category):
        labels = []
        for row in self.database:
            date, cat_obj, category = row
            if target_category.title() in category:
                labels.append(cat_obj.get_label())
        return labels

    def get_records_with_label(self, target_label):
        records = []
        for row in self.database:
            date, cat_obj, category = row
            if target_label == cat_obj.get_label():
                records.append(cat_obj)
        return records

    def get_records_in_category_ordered_by_labels(self, target_category):
        records = self.get_records_in_category(target_category)
        records.sort(key=lambda cat_obj: cat_obj.get_label())
        return records

    def print_records_in_category_ordered_by_labels(self, target_category):
        records = self.get_records_in_category_ordered_by_labels(target_category)
        for record in records:
            print(record)


if __name__ == '__main__':
    parser = Parser()
    mt = MoneyTracker(parser.parse_file('money_tracker.txt'))
    mt.create_database()
    print(mt)
    mt.add_record(datetime.strptime('22-03-2019', '%d-%m-%Y'), 250, 'loan', 'expense')
    mt.sort_database()
    # mt.print_records_in_date(datetime.strptime('22-03-2019', '%d-%m-%Y'))
    # print(mt.get_records_in_category_ordered_by_labels('income'))
    # # [print(row) for row in mt.database]

