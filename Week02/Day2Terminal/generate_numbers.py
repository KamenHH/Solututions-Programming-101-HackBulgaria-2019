# generate_numbers.py
import sys
from random import randint

def get_args():
    return (sys.argv[1], int(sys.argv[2]))

def generate_numbers(filename, numbers):
    num_list = [randint(1, 1000) for _ in range(numbers)]
    with open(filename, 'w') as f:
        for n in num_list:
            f.write(str(n) + ' ')
        f.write('\n')


def main():
    arguments = get_args()
    generate_numbers(arguments[0], arguments[1])

if __name__ == '__main__':
    main()