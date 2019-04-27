def letter_frequency(word):
    d = {}
    for letter in word:
        d[letter] = d.get(letter, 0) + 1
    return d
  

def anagrams(word1, word2):
    if len(word1) != len(word2):
        return 'NOT ANAGRAMS'
    if letter_frequency(word1.lower()) == letter_frequency(word2.lower()):
        return 'ANAGRAMS'
    return 'NOT ANAGRAMS'


def is_credit_card_valid(number):
    digit_list = [int(x) for x in str(number)]
    if len(digit_list) % 2 == 0:
        return False
    for i in range(1, len(digit_list), 2):
        digit_list[i] =  digit_list[i] * 2
    transformed_num = ''.join([str(num) for num in digit_list])
    check_sum = sum([int(num) for num in transformed_num])
    if check_sum % 10 == 0:
        return True
    return False

# print(is_credit_card_valid(79927398715))

def get_primes(n):
    from math import sqrt
    prime_list = [2]
    num = 3
    while num < n:
        if num % 2 == 0:
            num += 1
        elif int(sqrt(num)) == sqrt(num):
            num += 1
        else:
            for i in range(num//2-1, 2, -1):
                if num % i == 0:
                    break
            else:
                prime_list.append(num)
            num += 1
    return prime_list


def goldbach(n):
    result = []
    if n % 2 != 0:
        raise ValueError("Error, func goldbach(n) expected an even integer for n, got odd.")
    prime_list = get_primes(n)
    for prime in prime_list:
        difference = n - prime
        if difference in prime_list and (difference, prime) not in result:
            result.append((prime, difference))
    return result


# print(goldbach(100))

    
    
    