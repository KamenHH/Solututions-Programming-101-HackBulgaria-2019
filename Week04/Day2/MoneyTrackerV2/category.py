class Category:
    def __init__(self, amount, label):
        self._amount = amount
        self._label = label.title()

    def __str__(self):
        return str(self._amount) + ', ' + self._label
        
    def __repr__(self):
        return '(' + str(self) + ')'

    def get_label(self):
        return self._label

    def get_amount(self):
        return self._amount


class Expense(Category):
    CATEGORY_STR = 'New Expense'

    def __init__(self, amount, label):
        super().__init__(amount, label)


class Income(Category):
    CATEGORY_STR = 'New Income'

    def __init__(self, amount, label):
        super().__init__(amount, label)


if __name__ == '__main__':
    exp = Expense(10, 'coffee')
    exp2 = Expense(20, 'Gambling')
    inc = Income(520, 'Salary')
