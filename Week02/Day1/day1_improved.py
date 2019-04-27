def gas_stations(distance, tank_size, stations):
    # TODO: not improved
    # example = 320, 90, [50, 80, 140, 180, 220, 290]
    # [80, 140, 220, 290]
    ramaining_tank = tank_size - stations[0]
    output = []
    for i in range(1, len(stations)):
        if stations[i] - stations[i-1] > ramaining_tank:
            output.append(stations[i-1]) 
            ramaining_tank = tank_size - (stations[i] - stations[i-1])
        else:
            ramaining_tank -= stations[i] - stations[i-1]
    return output

print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290, 320]))

def is_number_balanced(n):
    digit_ls = [int(x) for x in str(n)]
    if len(digit_ls) %2 == 0:
        if sum(digit_ls[:len(digit_ls)//2]) == sum(digit_ls[len(digit_ls)//2:]):
            return True
    else:
        if sum(digit_ls[:len(digit_ls)//2]) == sum(digit_ls[len(digit_ls)//2+1:]):
            return True
    return False

def increasing_or_decreasing(seq):
    # TODO: not improved
    dec = 1
    inc = 1
    for i in range(1, len(seq)):
        if seq[i] < seq[i-1]:
            dec += 1
        elif seq[i] > seq[i-1]:
            inc += 1
        else:
            return False
    if inc == len(seq):
        return 'Up!'
    elif dec == len(seq):
        return 'Down!'
    else:
        return False

def get_largest_palindrome(n):
    string_n = str(n-1)
    while True:
        if string_n == string_n[::-1]:
            return int(string_n)
        string_n = str(int(string_n)-1)
    
# print(get_largest_palindrome(15998))

def sum_of_numbers(input_string):
    # with regex
    import re
    pattern = re.compile(r'\d+')
    return sum([int(x) for x in pattern.findall(input_string)])

def sum_of_numbers_iter(input_string):
    # without regex
    digits = ['0','1','2','3','4','5','6','7','8','9']
    buffer = ''
    sum_of_digits = 0
    for ch in input_string:
        if ch in digits:
            buffer += ch
        else:
            if buffer:
                sum_of_digits += int(buffer)
                buffer = ''
    if buffer:
        sum_of_digits += int(buffer)
    return sum_of_digits

# print(sum_of_numbers_iter('ab125cd3'))

def birthday_ranges(birthdays, ranges):
    # TODO: not improved 
    ranges = [range(r[0], r[1] + 1) for r in ranges]
    birtdays_per_range = []
    birthday_count = 0
    for r in ranges:
        for bday in birthdays:
            if bday in r:
                birthday_count += 1
        birtdays_per_range.append(birthday_count)
        birthday_count = 0
    return birtdays_per_range

lphabet = {
    '2': 'a',
    '22': 'b',
    '222': 'c',
    '3': 'd',
    '33': 'e',
    '333': 'f',
    '4': 'g',
    '44': 'h',
    '444': 'i',
    '5': 'j',
    '55': 'k',
    '555': 'l',
    '6': 'm',
    '66': 'n',
    '666': 'o',
    '7': 'p',
    '77': 'q',
    '777': 'r',
    '7777': 's',
    '8': 't',
    '88': 'u',
    '888': 'v',
    '9': 'w',
    '99': 'x',
    '999': 'y',
    '9999': 'z'
}

def get_key(seq_string):
    mod = 4 if '7' in seq_string or '9' in seq_string else 3
    multiplier = len(seq_string) % mod 
    return seq_string[0]*mod if multiplier == 0 else seq_string[0]*multiplier

def get_letter(buffer, caps):
    letter = alphabet[get_key(buffer)]
    return letter if caps is False else letter.upper()


def numbers_to_message(p_seq):
    from collections import deque
    msg = ''
    buffer = ''
    caps = False
    q = deque(p_seq)
    while q:
        curr_item = q.popleft()
        if curr_item == 1:
            caps = True
        elif curr_item == 0:
            msg += ' '
        elif curr_item == -1:
            continue
        elif curr_item not in (-1,0,1):
           buffer += str(curr_item)
           while q:
                if curr_item == q[0]:
                   buffer += str(q.popleft())
                else:
                    msg += get_letter(buffer, caps)
                    buffer = ''
                    caps = False
                    break
    msg += get_letter(buffer, caps)
    return msg

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


# print(message_to_numbers("Ivo e Panda"))

# print(numbers_to_message([1,7,7,7,8,8,2,2,9,9,9]))
    


def elevator_trips(people_weight, people_floors, elevator_floors, max_people, max_weight):
    in_elevator = []
    curr_weight = 0
    trip_count = 0
    people_count = 0
    curr_floor = 1
    people = [pair for pair in zip(people_weight, people_floors)]
    while people:
        while people and people_count + 1 <= max_people and curr_weight + people[0][0] <= max_weight:
            person = people.pop(0)
            in_elevator.append(person)
            curr_weight += person[0]
            people_count += 1
        while in_elevator:
            curr_person = in_elevator.pop(0)
            if curr_floor != curr_person[1]:
                curr_floor = curr_person[1]
                trip_count += 1
        curr_floor = 1
        trip_count += 1
        curr_weight = 0
        people_count = 0
    return trip_count

print(elevator_trips([40, 40, 100, 80, 60], [2, 3, 3, 2, 3], 3, 5, 200))
