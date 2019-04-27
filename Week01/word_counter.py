dirs = {
    'hor_left_right': (0, 1),
    'hor_right_left': (0, -1),
    'vert_tom_bottom': (1, 0),
    'vert_bottom_top': (-1, 0),
    'diag_r_top_bottom': (1, 1),
    'diag_r_bottom_top': (-1, -1),
    'diag_l_top_bottom': (1, -1),
    'diag_l_bottom_top': (-1, 1)
}


def build_grid(string):
    string = string.replace(' ', '')
    grid = []
    row = []
    for ch in string:
        if ch != '\n':
            row.append(ch)
        else:
            grid.append(row.copy())
            row.clear()
    return grid


def find_pattern(grid, row, col, word):
    matches = 0
    if len(word) > row or len(word) > col:
        return False

    for r in range(row):
        for c in range(col):
            if grid[r][c] != word[0]:
                continue
            else:
                matches += build_pattern(grid, r, c, word)
    if word == word[::-1]:
        matches //= 2
    return matches


def build_pattern(grid, r, c, word):
    match = 0
    for d in dirs:
        curr_row = r
        curr_col = c
        for i in range(1, len(word)):
            curr_row += dirs[d][0]
            curr_col += dirs[d][1]
            if curr_row < 0 or curr_col < 0:
                break
            try:
                if grid[curr_row][curr_col] != word[i]:
                    break
            except IndexError:
                break
        else:
            match += 1
    return match


def main():
    string1 = '''i v a n
e v n h
i n a v
m v v n
q r i t
'''
    string2 = '''i v a n q h r e z g t z o y m
e v n h t r x e k y d a i l c
i a c t u a l l y m c x r l e
m v c n p u a m n t l u e a a
q r i t w e a q u p r x t u z
p e a c t u a l l y w p y t m
o y h t r e l u f p q n z c s
p a c t u a l l y u r e q a r
'''
    string3 = '''z v a n q h r e z g t z
e v m h t r x e k y m a
i a c a u a l l y a c x
m v c n d u a m d t l u
q t i t w a a a u p r x
p e m a d a m l l y w p
o y h t e e l u f p q n
p a c t u a l l y u r e
'''

    row = 8
    col = 15
    word = 'actually'

    grid = build_grid(string2)
    for r in grid:
        print(r)
    print(find_pattern(grid, row, col, word))


if __name__ == '__main__':
    main()
