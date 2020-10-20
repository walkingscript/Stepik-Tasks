"""Транспонирование матрицы
На вход поступают размеры матрицы n и m.
Затем построчно матрица.
Результат: транспонированная матрица."""


def get_matrix(count_of_lines: int) -> list:
    matrix = []
    for _ in range(count_of_lines):
        matrix.append(list(map(int, input().split())))
    return matrix


def transp(matrix: list) -> list:
    _, m = len(matrix), len(matrix[0])
    res_mat = [[] for i in range(m)]
    for line in matrix:
        for number, item in enumerate(line):
            res_mat[number].append(item)
    return res_mat


def print_mat(matrix):
    for line in matrix:
        mat_str = map(str, line)
        print(' '.join(mat_str))


def main():
    n, _ = map(int, input().split(' '))
    mat = get_matrix(n)
    transp_mat = transp(mat)
    print_mat(transp_mat)
    

if __name__ == '__main__':
    main()
