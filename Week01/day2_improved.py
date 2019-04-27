def sum_of_digits(n):
    return sum([int(i) for i in str(abs(n))])

    
def to_digits(n):
    return [int(i) for i in str(n)]

    
def to_number(li):
    return ''.join([str(i) for i in li])


def fact_digits(num):
    def fact(n):
        factorial = 1
        while n != 1:
            factorial *= n
            n -= 1
        return factorial

    return sum([fact(int(ch)) for ch in str(num)])


def palindrome(n):
    return str(n) == str(n)[::-1]


def char_histogram_(string):
    histogram = {}
    for c in string:
        histogram[c] = histogram.get(c, 0) + 1
    return histogram


def sum_metrix(matrix):
    return sum([sum(m) for m in matrix])


def nan_expand(n):
    if n == 0:
        return ""
    return "Not a "*n + "NaN"