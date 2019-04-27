# sum_numbers.py
import sys
from random import randint

def get_args():
    return sys.argv[1]

def sum_numbers(filename):
    with open(filename) as f:
        numbers = f.read()
    numbers = [int(x) for x in numbers.split(' ') if x != '\n']
    return sum(numbers)



def main():
    arguments = get_args()
    print(sum_numbers(arguments))

if __name__ == '__main__':
    main()