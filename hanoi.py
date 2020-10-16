DECISIONS = {0: ((1, 2), (1, 3), (2, 3)), 
             1: ((1, 3), (1, 2), (2, 3))}


def rotate_list(lst):
    while True:
        for item in lst:
            yield item


def calculate_steps(hanoi: dict, decision) -> None:
    source = hanoi[1][::]
    for a, b in rotate_list(decision):
        from_, to = a, b
        if len(hanoi[a]) > 0 and len(hanoi[b]) > 0: 
            if hanoi[a][-1] > hanoi[b][-1]:
                from_, to = b, a
        else:
            if len(hanoi[a]) == 0:
                from_, to = b, a
            else:
                from_, to = a, b
        hanoi[to].append(hanoi[from_].pop())      
        
        print(from_, '-', to)

        if hanoi[3] == source:
            break


def main():
    n = int(input())
    decision = DECISIONS[n % 2]
    hanoi = {1: [ring for ring in range(n, 0, -1)], 2: [], 3: []}
    calculate_steps(hanoi, decision)


if __name__ == '__main__':
    main()