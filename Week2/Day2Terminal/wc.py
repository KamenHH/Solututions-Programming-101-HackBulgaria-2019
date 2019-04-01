# wc.py
import sys

def get_args():
    return sys.argv[1], sys.argv[2]

def wc(command, textfile):
    count = 0
    with open(textfile) as file:
        content = file.readlines()
    if command == 'lines':
        return len(content)
    for line in content:
        if command == 'chars':
            count += len(line)
        elif command == 'words':
            count += len(line.split())
    return count



def main():
    command, filename = get_args()
    print(wc(command, filename))


if __name__ == '__main__':
    main()