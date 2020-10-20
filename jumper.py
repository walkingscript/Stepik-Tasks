def is_jolly_jumper(sequence: list) -> str:
    '''Функция определяет является ли последовательность
    целых чисел, которая поступает на вход, jolly jumper
    последовательностью.'''
    length = len(sequence)
    if length == 1:
        return 'Jolly'
    abs_seq = [
        abs(sequence[i] - sequence[i-1])
        for i in range(1, len(sequence))
    ]
    for x in range(1, length):
        if x not in abs_seq:
            return 'Not jolly'
    return 'Jolly'


def main():
    sequence = list(map(int, input().split()))
    result = is_jolly_jumper(sequence)
    print(result)


if __name__ == '__main__':
    main()