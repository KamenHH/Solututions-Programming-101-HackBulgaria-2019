# cat.py
import sys

def get_args():
    return sys.argv[1]


def cat(arguments):
    with open(arguments) as f:
        content = f.readlines()
        for line in content:
            print(line.strip())


def main():
    arguments = get_args()
    cat(arguments)

if __name__ == '__main__':
    main()