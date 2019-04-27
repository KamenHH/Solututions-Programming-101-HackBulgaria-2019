class Category:
    def __init__(self, amount, label):
        self._amount = amount
        self._label = label

    def __str__(self):
        return str(self._amount) + ', ' + self._label
        
    def __repr__(self):
        return str(self)

    def get_label(self):
        return self._label


class Expense(Category):
    def __init__(self, amount, label):
        super().__init__(amount, label)
        self.STR = 'New Expense'



class Income(Category):
    def __init__(self, amount, label):
        super().__init__(amount, label)
        self.STR = 'New Expense'