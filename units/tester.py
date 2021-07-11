from itertools import permutations
from random import randint

from main import UNITS


def main():
    data = list(permutations(UNITS.keys(), 2))

    with open('in', 'w') as f:
        for from_, to_ in data:
            in_ = f'{randint(0, 10000)} {from_} in {to_}'
            print(in_, file=f)


if __name__ == '__main__':
    main()
