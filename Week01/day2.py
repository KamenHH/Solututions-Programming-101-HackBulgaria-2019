def sum_of_digits(number):
    str_num = str(abs(number))
    n_sum = 0
    for i in str_num:
        n_sum += int(i)
    return n_sum


def to_digits(n):
    str_n = str(n)
    list_n = []
    for i in str_n:
        list_n.append(int(i))
    return list_n


def to_number(li):
    str_n = ''
    for i in li:
        str_n += str(i)
    return int(str_n)


def fact_digits(num):
    def fact(n):
        factorial = 1
        while n != 1:
            factorial *= n
            n -= 1
        return factorial

    str_num = str(num)
    result = 0

    for i in str_num:
        result += fact(int(i))
    return result


def palindrome(n):
    return str(n) == str(n)[::-1]


def count_vowels(string):
    vowels = 'aeiouy'
    count = 0

    for c in string:
        if c.lower() in vowels:
            count += 1
    return count


def count_constants(string):
    constants = 'bcdfghjklmnpqrstvwxz'
    count = 0

    for c in string:
        if c.lower() in constants:
            count += 1
    return count


def char_histogram(string):
    char_dict = {}

    for c in string:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict


def sum_metrix(matrix):
    m_sum = 0
    for m in matrix:
        m_sum += sum(m)
    return m_sum


def nan_expand(n):
    if n == 0:
        return ""
    return "Not a "*n + "NaN"


def prime_factorization(n):
    result = []
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    groups = group(factors)
    for g in groups:
        result.append((g[0], len(g)))
    return result


def group(items):
    groups = []
    temp_group = []
    skip = 1
    for i in range(len(items)):
        if skip != 1:
            skip -= 1
            continue
        temp_group.append(items[i])
        for j in range(i+1, len(items)):
            if items[i] == items[j]:
                temp_group.append(items[i])
                skip += 1
            else: 
                break
        groups.append(temp_group.copy())
        temp_group.clear()
    return groups


def max_consecutive(items):
    curr_max = 1
    temp_max = 1
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i] == items[j]:
                temp_max += 1
            else:
                break
        if temp_max > curr_max:
            curr_max = temp_max
        temp_max = 1
    return curr_max

def main():
    print(sum_metrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))

main()