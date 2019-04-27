letter_encoding = {
    'a': '2',
    'b': '22',
    'c': '222',
    'd': '3',
    'e': '33',
    'f': '333',
    'g': '4',
    'h': '44',
    'i': '444',
    'j': '5',
    'k': '55',
    'l': '555',
    'm': '6',
    'n': '66',
    'o': '666',
    'p': '7',
    'q': '77',
    'r': '777',
    's': '7777',
    't': '8',
    'u': '88',
    'v': '888',
    'w': '9',
    'x': '99',
    'y': '999',
    'z': '9999',
    ' ': '0'
}

def append_code(numbers, code):
    code_nums = [int(x) for x in code]
    while code_nums:
        numbers.append(code_nums.pop(0))

def message_to_numbers(message):
    numbers = []
    for ch in message:
        if ord(ch) in range(65, 91):
            numbers.append(1)
            append_code(numbers, letter_encoding[ch.lower()])
        elif ch in letter_encoding:
            try:
                if str(numbers[-1]) in letter_encoding[ch]:
                    numbers.append(-1)
                    append_code(numbers, letter_encoding[ch])
                elif numbers[-1] == -1:
                    append_code(numbers, letter_encoding[ch])
                    numbers.append(-1)
                else:
                    append_code(numbers, letter_encoding[ch])
            except IndexError: 
                append_code(numbers, letter_encoding[ch])
                numbers.append(-1)
    if numbers[-1] == -1:
        return numbers[:-1]
    return numbers
