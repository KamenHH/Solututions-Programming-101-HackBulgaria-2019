from parse_money_tracker_data import Parser
from category import Expense, Income

class MoneyTracker:
    def __init__(self, content):
        self.user_data = {}
        for line in content:
            if '=' in line:
                curr_date = line.strip('=\n ')
                self.user_data[curr_date] = {'income': [], 'expense': []}
            else:
                amount, label, category = line.split(', ')
                amount = MoneyTracker.int_or_float(float(amount))
                if 'income' in category.lower():
                    self.user_data[curr_date]['income'].append(Income(amount, label))
                elif 'expense' in category.lower():
                    self.user_data[curr_date]['expense'].append(Expense(amount, label))
    
    
    def list_user_data(self):
        # check __call__
        for date in self.user_data:
            print('=== {} ==='.format(date))
            for category in self.user_data[date]:
                for cat_obj in self.user_data[date][category]:
                    print('{}, {}'.format(cat_obj, cat_obj.STR))
    
    def _incomes(self):
        incomes = []
        for date in self.user_data:
            try:
                incomes += self.user_data[date]['income']
            except KeyError:
                return []
        return incomes

    def _expenses(self):
        expenses = []
        for date in self.user_data:
            try:
                expenses += self.user_data[date]['expense']
            except KeyError:
                return []
        return expenses

    def _savings(self):
        result = [cat_obj for date in self.user_data
                for cat_obj in self.user_data[date]['income']
                if cat_obj.get_label() == 'Savings']
        return result
    
    def _deposits(self):
        result = [cat_obj for date in self.user_data
                for cat_obj in self.user_data[date]['income']
                if cat_obj.get_label() == 'Deposit']
        return result

    def _get_user_expenses_ordered_by_categories(self):
        expenses = self._expenses()
        return sorted(expenses, key=lambda expense: expense.get_label())
    
    def print_user_expenses_ordered_by_categories(self):
        print('Expenses by categories: ')
        for expense in self._get_user_expenses_ordered_by_categories():
            print(expense)

    
    @staticmethod
    def int_or_float(n: float):
        return int(n) if n.is_integer() else n

if __name__ == '__main__':
    parser = Parser('money_tracker.txt')
    mt = MoneyTracker(parser.content())
    print(mt.list_user_data())