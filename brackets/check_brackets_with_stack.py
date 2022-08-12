import collections

Bracket = collections.namedtuple("Bracket", "value, position")
brackets = {')': '(', ']': '[', '}': '{'}


def test_code(string):
    stack = collections.deque()
    result = True
    ret: int = 0

    for number, char in enumerate(string, 1):

        if char in brackets.values():  # if it is opening bracket
            stack.append(Bracket(char, number))

        if char in brackets.keys():  # if it is closing bracket

            if stack:
                if stack[-1].value == brackets[char]:
                    stack.pop()
                    continue

            ret = number
            result = False
            break

    else:
        if stack:
            ret = stack[-1].position
            result = False

    print("Success" if result else ret)


def main():
    while True:
        try:
            test_code(input())
        except EOFError:
            break


if __name__ == '__main__':
    main()
