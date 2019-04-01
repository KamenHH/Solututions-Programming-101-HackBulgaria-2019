def matrix_bombing_plan(m):
    damage_count = {}
    for row in range(len(m)):
        for col in range(len(m[0])):
            damage_count[(row, col)] = drop_bomb(m, row, col, m[row][col])
    return damage_count


def drop_bomb(m, r, c, curr_item):
    from copy import deepcopy
    temp_m = deepcopy(m)
    damage_sum = 0
    positions = {
        'left': (0, -1),
        'right': (0, 1),
        'top': (-1, 0),
        'bottom': (1, 0),
        'topleft': (-1, -1),
        'topright': (-1, 1),
        'bottomleft': (1, -1),
        'bottomright': (1, 1)
    }
    for pos in positions:
        row = r + positions[pos][0]
        col = c + positions[pos][1]
        if row >= 0 and col >= 0:
            try:
                temp_m[row][col] = temp_m[row][col] - curr_item if temp_m[row][col] - curr_item >= 0 else 0
            except IndexError:
                continue
    return sum([sum(row) for row in temp_m])


def print_result(result):
    for k, v in result.items():
        print(k, v)


def main():
    results = matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print_result(results)

if __name__ == '__main__':
    main()
