import sys


def get_input():
    """Reads key-value pairs from the stdin, one on each line."""
    pairs = []
    print("Enter key-value pairs separated with an interval(space).\nTo exit, pres Ctrl + D.")
    for line in sys.stdin:
        pair = line.split(sep=' ')
        if len(pair) != 2:
            print("Input should be a single pair on a single line!")
            continue
        key = pair[0]
        try:
            value = int(pair[1])
        except ValueError:
            print("Incorrect value provided, please try again!")
            continue
        else:
            if value < 0:
                print("Value must be a positive integer!")
                continue
        pairs.append((key, value))
    return pairs
            

def reduce(input_list):
    """Creates a dictionary from the given input, each key is unique."""
    dictionary = {}
    for item in input_list:
        key, value = item
        if key not in dictionary:
            dictionary[key] = value
        else:
            dictionary[key] += value
    return dictionary


def get_top3(dictionary):
    """Returns the 3 elements with the highest values."""
    item_list = list(dictionary.items())
    if len(item_list) >= 3:
        item_list.sort(key=lambda pair: pair[1], reverse=True)
        return item_list[:3]
    return None


def _print_output(diff_pair, pair_list, no_equal=False):
    """Prints the output provided by output_result function."""
    if diff_pair is None and no_equal is False:
        pair_list.sort(key=lambda pair: pair[0])  # alphabetically
        print("{}, {}, {}: {}".format(pair_list[0][0], pair_list[1][0],
                                      pair_list[2][0], pair_list[0][1]))
    elif no_equal:
        for pair in pair_list:
            print(pair[0], pair[1])
    elif diff_pair[1] > pair_list[0][1]:
        print(diff_pair[0] + ' ' + str(diff_pair[1]) + '\n' +
              pair_list[0][0] + ', ' + pair_list[1][0] + ': ' + str(pair_list[0][1]))
    elif diff_pair[1] < pair_list[0][1]:
        print(pair_list[0][0] + ', ' + pair_list[1][0] + ': ' + str(pair_list[0][1]) + '\n' +
              diff_pair[0] + ' ' + str(diff_pair[1]))
    print('\n')


def output_builder(top3):
    """Builds the output end result."""
    if top3:
        temp = top3.copy()
        if temp[0][1] == temp[1][1] and temp[1][1] != temp[2][1]:
            _print_output(temp.pop(2), temp)
        elif temp[1][1] == temp[2][1] and temp[2][1] != temp[0][1]:
            _print_output(temp.pop(0), temp)
        elif temp[2][1] == temp[0][1] and temp[0][1] != temp[1][1]:
            _print_output(temp.pop(1), temp)
        elif temp[0][1] == temp[1][1] and temp[1][1] == temp[2][1]:
            _print_output(None, temp)
        else:
            _print_output(None, top3, no_equal=True)
    else:
        print("Not sufficient key-value pairs to evaluate!")


def main():
    data = get_input()
    dictionary = reduce(data)
    print(dictionary)
    top3 = get_top3(dictionary)
    output_builder(top3)


if __name__ == '__main__':
    main()
