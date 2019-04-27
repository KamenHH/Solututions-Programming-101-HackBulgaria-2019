import csv


def read_csv_file(filename):
    try:
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            data = [row for row in csv_reader]
    except FileNotFoundError:
        print('Error, file specified not found in current directory!')
        return None
    return data


def validate_keys(data, kwargs):
    columns_in_table = data[0]
    for key in kwargs.keys():
        if key not in columns_in_table:
            return False
    return True


def filter(csv_data, full_name__startswith=None, email__contains=None,
           salary__gt=None, salary__lt=None, order_by=None, **kwargs):
    matched_rows = []
    are_keys_valid = validate_keys(csv_data, kwargs)
    for row in csv_data[1:]:
        kwargs_in_row = True
        if are_keys_valid:
            for arg_value in kwargs.values():
                if arg_value not in row:
                    kwargs_in_row = False
                    break  # !
        if kwargs_in_row and are_keys_valid:
            if full_name__startswith:
                if not full_name_startswith(row, full_name__startswith):
                    continue
            if email__contains:
                if not email_contains(row, email__contains):
                    continue
            if salary__gt and salary__lt:
                gt = greater_than(row, salary__gt)
                lt = less_than(row, salary__lt)
                if not gt or not lt:
                    continue
            elif salary__gt:
                if not greater_than(row, salary__gt):
                    continue
            elif salary__lt:
                if not less_than(row, salary__lt):
                    continue
            matched_rows.append(row)
    if order_by == 'salary':
        order_data_by(matched_rows)
    return matched_rows


def count(csv_data, full_name__startswith=None, email__contains=None,
          salary__gt=None, salary__lt=None, order_by=None, **kwargs):
    data = filter(csv_data, full_name__startswith, email__contains,
                  salary__gt, salary__lt, order_by, **kwargs)
    return len(data)


def first(csv_data, full_name__startswith=None, email__contains=None,
          salary__gt=None, salary__lt=None, order_by=None, **kwargs):
    data = filter(csv_data, full_name__startswith, email__contains,
                  salary__gt, salary__lt, order_by, **kwargs)
    if data:
        return data[0]
    return None


def last(csv_data, full_name__startswith=None, email__contains=None,
          salary__gt=None, salary__lt=None, order_by=None, **kwargs):
    data = filter(csv_data, full_name__startswith, email__contains,
                  salary__gt, salary__lt, order_by, **kwargs)
    if data:
        return data[-1]
    return None


def full_name_startswith(row, full_name__startswith):
    first_name = row[0]
    return True if first_name[:len(full_name__startswith)] == full_name__startswith else False


def email_contains(row, email__contains):
    email = row[3]
    return True if email[len(email)-len(email__contains):] == email__contains else False


def greater_than(row, salary__gt):
    return True if int(row[-1]) > salary__gt else False


def less_than(row, salary__lt):
    return True if int(row[-1]) < salary__lt else False


def order_data_by(matched_rows):
    matched_rows.sort(key=lambda row: int(row[-1]))


def print_result(results):
    for row in results:
        for field in row:
            print(field, end=', ')
        print('')


if __name__ == '__main__':
    data = read_csv_file('dummy_file.csv')
    print_result(filter(data, not_an_argument=''))
    # print_result(filter(data, email__contains='@yahoo.com', order_by='salary'))
    # print(count(data, email__contains='@yahoo.com', order_by='salary'))
    # print(first(data, email__contains='@yahoo.com', order_by='salary'))
    # print(last(data, email__contains='@yahoo.com', order_by='salary'))
