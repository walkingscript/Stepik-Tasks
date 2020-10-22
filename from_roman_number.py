rcs = {
  'I': 1, 'V': 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000
}


def transform_from_roman(roman_number: str):
    rn_len = len(roman_number)
    number = 0
    for i in range(0, rn_len):
        if i+1 != rn_len:
            if rcs[roman_number[i+1]] > rcs[roman_number[i]]:
                number -= rcs[roman_number[i]]
                continue
        number += rcs[roman_number[i]]
    return number


def main():
    roman_number = input()
    number = transform_from_roman(roman_number)
    print(number)


if __name__ == "__main__":
    main()
