NUMBERS = {
    '0': (' -- ', '|  |', '|  |', '    ', '|  |', '|  |', ' -- '),
    '1': ('    ', '   |', '   |', '    ', '   |', '   |', '    '), 
    '2': (' -- ', '   |', '   |', ' -- ', '|   ', '|   ', ' -- '), 
    '3': (' -- ', '   |', '   |', ' -- ', '   |', '   |', ' -- '), 
    '4': ('    ', '|  |', '|  |', ' -- ', '   |', '   |', '    '), 
    '5': (' -- ', '|   ', '|   ', ' -- ', '   |', '   |', ' -- '), 
    '6': (' -- ', '|   ', '|   ', ' -- ', '|  |', '|  |', ' -- '), 
    '7': (' -- ', '   |', '   |', '    ', '   |', '   |', '    '), 
    '8': (' -- ', '|  |', '|  |', ' -- ', '|  |', '|  |', ' -- '), 
    '9': (' -- ', '|  |', '|  |', ' -- ', '   |', '   |', ' -- ')
}
HEIGHT = len(NUMBERS['0'])
EMPTY_SPACE = ' '
CORNER = 'x'
TOP = '-'
SIDE = '|'
    

def main():
    num = input()
    top = bottom = ''.join((
        CORNER,
        TOP * (len(num) * len(NUMBERS['0'][1]) + len(num)-1),
        CORNER
    ))
    print(top)

    for i in range(HEIGHT):
        s = ''.join((SIDE, 
                    EMPTY_SPACE.join([NUMBERS[key][i] for key in num]), 
                    SIDE))
        print(s)

    print(bottom)


if __name__ == '__main__':
    main()
