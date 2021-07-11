"""Сапёр. Выводит "решённое" поле, т.е. для каждой ячейки,
не являющейся миной, указывается число мин, находящихся 
в соседних ячейках (учитывая диагональные направления)"""


n, m = map(int, input().split(' '))

field = []

neighbours = ((0,1), (1,1), (1,0), (1,-1),
            (0,-1), (-1,-1), (-1,0), (-1,1))

for i in range(n):
    field.append(list(input()))

for i in range(n):
    for j in range(m):
        if field[i][j] == '*':
            continue        
        count = 0
        for x, y in neighbours:
            try:
                pos1 = i + x
                pos2 = j + y
                if pos1 < 0 or pos2 < 0:
                    continue
                if field[i+x][j+y] == '*':
                    count += 1
            except IndexError:
                continue
        field[i][j] = str(count)


for line in field:
    print(''.join(line))
