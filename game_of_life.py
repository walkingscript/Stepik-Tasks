def print_field(field: list) -> None:
    for line in field:
        print(''.join(line))


def get_next_field(field: list, size: tuple) -> list:
    n, m = size
    neighbour_cells = ((0, 1), (1, 1), (1, 0), (1, -1),
                       (0, -1), (-1, -1), (-1, 0), (-1, 1))
    next_field = [[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            neighbors = []
            for x, y in neighbour_cells:
                try:
                    pos1 = i + x
                    if pos1 == n:
                        pos1 = 0
                    pos2 = j + y 
                    if pos2 == m:
                        pos2 = 0
                    neighbors.append(field[pos1][pos2])
                except IndexError:
                    continue
            state = field[i][j]
            if state == '.' and neighbors.count('X') == 3:
                next_field[i].append('X')
            elif state == 'X' and neighbors.count('X') < 2 \
                              or neighbors.count('X') > 3:
                next_field[i].append('.')
            else:
                next_field[i].append(state)
    return next_field
    

def main():
    n, m = map(int, input().split())
    field = []
    for _ in range(n):
        line = list(input())
        if len(line) == m:
            field.append(line)
        else:
            raise ValueError
    next_field = get_next_field(field, (n, m))
    print_field(next_field)


if __name__ == "__main__":
    main()
