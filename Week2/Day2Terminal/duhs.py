# duhs.py
import sys
from os.path import getsize, join
from os import chdir, walk

def get_args():
    return sys.argv[1]


def duhs(filepath):
    total_size = 0
    for dirpath, dirnames, filenames in walk(filepath):
        for file in filenames:
            # print(join(dirpath, file))
            # print(getsize(join(dirpath, file)))
            curr_file = join(dirpath, file)
            total_size += getsize(curr_file)
    return total_size/2048, filepath



def main():
    arguments = get_args()
    result = duhs(arguments)
    print(result[0], result[1])

if __name__ == '__main__':
    main()