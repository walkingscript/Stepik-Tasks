'''
На вход поступают карты в формате значение-масть и козырь.
Программа определяет бьёт ли одна карта другую.
Пример входных данных: 
    AS KH
    H
Результат:
    Second
'''
import re


CARDS = ('6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')


def judge(card_1: tuple, card_2: tuple, trump: str):
    value1, suit_1, value_2, suit_2 = *card_1, *card_2
    # если карты разных мастей и есть козыри
    if suit_1 != suit_2 and (suit_1 == trump or suit_2 == trump):
        # карта с козырной мастью побеждает
        if suit_1 == trump:
            return 'First'
        if suit_2 == trump:
            return 'Second'

    # если карты разных мастей и нет козырей
    if suit_1 != suit_2 and (suit_1 != trump or suit_2 != trump):
        return 'Error'

    # если карты одной масти
    if suit_1 == suit_2:
        if CARDS.index(value_1) > CARDS.index(value_2):
            return 'First'
        else:
            return 'Second'


def main():
    _in = input().upper()
    trump = input().upper()

    regex = re.compile('(6|7|8|9|10|J|Q|K|A)(C|D|H|S)')
    card_1, card_2 = regex.findall(_in)

    print(judge(card_1, card_2, trump))


if __name__ == "__main__":
    main()
