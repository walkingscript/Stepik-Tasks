"""
На вход поступает число n.
Возвращает число, закодированное в римской системе счисления.
"""
from collections import OrderedDict, ChainMap
from functools import reduce


ROMAN_NUMBERS = OrderedDict(
    {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
)

NUMBER_EXCEPTIONS = {
    4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'
}

search_dict = ChainMap(ROMAN_NUMBERS, NUMBER_EXCEPTIONS)


def divide_to_parts(n: int):
    parts = []
    for k, _ in ROMAN_NUMBERS.items():
        if n < k:
            continue
        count = n // k
        parts.append([k for i in range(count)])
        n -= count * k
    return parts


def to_full_list_sequence(sequence: list):
    """
    Возвращает список, элементами которого являются
    только списки с уровнем вложенности 0.
    """
    return [x if type(x) is list else [x,] for x in sequence]


def make_roman_numbers(sequence: list[int]):
    """
    Преобразует последовательность чисел таким образом,
    чтобы её можно было преобразовать в строку с римскими
    числами с максимальной эффективностью.
    """
    # 1-ое правило
    i = 1
    while i < len(sequence):
        x = sum(sequence[i-1]) + sum(sequence[i])
        if x in NUMBER_EXCEPTIONS:
            sequence[i-1:i+1] = [[x]]
            continue
        i += 1
    # 2-ое правило
    for i in range(len(sequence)):
        x = sum(sequence[i])
        if x in NUMBER_EXCEPTIONS:
            sequence[i] = [x]
    return sequence


def roman(number: int):
    parts = to_full_list_sequence(divide_to_parts(number))
    parts = make_roman_numbers(parts)
    # сглаживание списка
    parts = reduce(lambda x, y: x + y, parts)
    return ''.join([search_dict[item] for item in parts])


def main():
    n = int(input())
    result = roman(n)
    print(result)


if __name__ == "__main__":
    main()
