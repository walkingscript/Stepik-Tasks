neibours = ((0, 1), (1, 1), (1, 0), (1, -1), 
            (0, -1), (-1, -1), (-1, 0), (-1, 1))
n, m = map(int, input().split())
field = []
for i in range(n):
    line = list(input())
    if len(line) == m:
        field.append(line)
    else:
        raise ValueError

next_field = []

for i in range(n):
    for j in range(m):
        count_live_cells = 0
        for x, y in neibours:
            try:
                pos1 = i + x
                pos2 = j + y
                if pos1 < 0 or pos2 < 0:
                    continue
                if field[pos1][pos2] == 'X':
                    count_live_cells += 1
            except IndexError:
                continue
        # в мёртвой клетке, вокруг которой ровно 3 живые клетки - зарождается жизнь
        if field[i][j] == '.' and count_live_cells == 3:
            next_field.append('X')
        # если у живой клетки есть две или три живые соседки
        elif field[i][j] == 'X' and count_live_cells not in (2, 3):
            #то эта клетка продолжает жить
            next_field.append('.')
        else:
            next_field[i].append(field[i][j])

for line in next_field:
    print(''.join(line))