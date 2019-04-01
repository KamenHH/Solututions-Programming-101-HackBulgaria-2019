# cat2.py
import sys

def get_args():
    return sys.argv[1:]


def cat2(arguments):
    for arg in arguments:
        with open(arg) as f:
            content = f.readlines()
            for line in content:
                print(line.strip())
            print('')


def main():
    arguments = get_args()
    cat2(arguments)

if __name__ == '__main__':
    main()