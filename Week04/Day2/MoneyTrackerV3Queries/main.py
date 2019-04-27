from sys import stdin

tokens = []
for line in stdin:
    line = line.strip('\n')

    tokens += line.split(' ')
print(tokens)

