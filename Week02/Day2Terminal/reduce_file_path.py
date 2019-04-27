# reduce_file_path.py
import sys

def get_args():
    return sys.argv[1]

def reduce_file_path(path):
    reduced_path = []
    for ch in path.split('/'):
        if ch == '..' and reduced_path:
            reduced_path.pop()
        elif ch != '' and ch != '.' and ch != '..':
            reduced_path.append('/' + ch)
    return ''.join(reduced_path) if reduced_path else '/'


def main():
    path = get_args()
    print(reduce_file_path(path))

if __name__ == '__main__':
    main()