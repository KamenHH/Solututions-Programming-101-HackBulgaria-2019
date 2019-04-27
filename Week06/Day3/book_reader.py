import os
DIR_PATH = 'Book'


def reader():
    files = os.listdir(DIR_PATH)
    os.listdir(DIR_PATH).sort()
    for file in files:
        with open(os.path.join(DIR_PATH, file)) as f:
            line = f.readline() 
            while True:    
                try:  
                    while line[0] != '#':
                        yield line
                        line = f.readline()
                    input()
                    yield line
                    line = f.readline()
                except IndexError:
                    break


def main():
    for line in reader():
        print(line)


if __name__ == '__main__':
    main()


# def reader():
#     for file in os.listdir(DIR_PATH):
#         with open(os.path.join(DIR_PATH, file)) as f:
#             line = f.readline()    
#             while True:      
#                 if line[0] == '#':
#                     yield line
#                     line = f.readline()
#                 else:
#                     try:
#                         while line[0] != '#':
#                             yield line
#                             line = f.readline()
#                         input()
#                     except IndexError:
#                          break