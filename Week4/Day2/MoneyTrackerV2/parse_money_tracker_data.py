class Parser:
    def __init__(self):
        pass

    def parse_file(self, filename):
        try:
            with open(filename) as dbfile:
                content = dbfile.readlines()
            return [line.strip('\n') for line in content]
        except FileNotFoundError:
            return None

    def get_amount(self):
        parsed_amount = self._read_amount()
        return int(parsed_amount) if isinstance(parsed_amount, float) \
                                     and parsed_amount.is_integer() else parsed_amount

    def _read_amount(self):
        while True:
            amount = input('amount: ')
            valid_amount = self._parse_amount(amount)
            if valid_amount:
                return valid_amount
            print('Invalid input for amount! Please, try again.')

    def _parse_amount(self, amount):
        for num_type in (int, float):
            try:
                value = num_type(amount)
            except ValueError:
                continue
            else:
                if value > 0:
                    return value
        return None

    def get_date(self):
        return self._read_date()

    def _read_date(self):
        while True:
            date = input('date: ')
            valid_date = self._parse_date(date)
            if valid_date:
                return valid_date

    def _parse_date(self, date):
        from datetime import datetime
        try:
            date = datetime.strptime(date, '%d-%m-%Y')
            return date
        except ValueError:
            print("Error, provided date not in correct format, expected Day-Month-Year, got {}".format(date))
            return None


if __name__ == '__main__':
    parses = Parser()
    print(parses.get_amount())
