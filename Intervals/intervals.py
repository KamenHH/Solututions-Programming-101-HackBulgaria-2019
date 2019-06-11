import sys


def get_input():
    """Gets user input from stdin"""
    print("Enter integers, one per line. To exit press Ctrl+D:")
    data = []
    for line in sys.stdin:
        line = line.strip('\n')
        try:
            line = int(line)
        except ValueError:
            print('Error, provided data not an integer!')
        else:
            data.append(line)
    return data


def sort_data(input_data):
    """Sorts the input data."""
    input_data.sort()
    return input_data


def build_intervals(sorted_data):
    """Builds consecutive intervals from the sorted data."""
    intervals = []
    count = 1
    for i in range(len(sorted_data)):
        if count != 1:
            count -= 1
            continue
        start = end = sorted_data[i]
        for j in range(i+1, len(sorted_data)):
            if sorted_data[j] - start == abs(count):
                end = sorted_data[j]
                count += 1
            else:
                break
        intervals.append((start, end, count))
    return intervals


def print_intervals(intervals):
    """Print output intervals."""
    for interval in intervals:
        print('[{}, {}] with consecutive count of {}'.
              format(interval[0], interval[1], interval[2]))
    print('\n')


def main():
    data = get_input()
    sorted_data = sort_data(data)
    intervals = build_intervals(sorted_data)
    print_intervals(intervals)


if __name__ == '__main__':
    main()

