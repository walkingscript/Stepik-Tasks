"""
Through standard input program receiving strings with units that needs to be converted and returns result.

Input string format:

    {quantity} {unit_name_that_needs_to_be_converted} in {unit_name_to_convert_quantity}

Example:

    5298 mile in foot
"""


import re
import sys

from collections import namedtuple

Unit = namedtuple('Unit', 'quantity, unit_name')

UNITS = {
    'mile': Unit(1609, 'm'),
    'yard': Unit(0.9144, 'm'),
    'foot': Unit(30.48, 'cm'),
    'inch': Unit(2.54, 'cm'),
    'km': Unit(1000, 'm'),
    'm': Unit(100, 'cm'),
    'cm': Unit(0.01, 'm'),
    'mm': Unit(0.001, 'm')
}

input_pattern = re.compile(r'(?P<quantity>[0-9.]+) (?P<unit_from>\w+) in (?P<unit_to>\w+)')


def convert(value, from_, to_):
    unit_from_value = UNITS[from_]
    unit_to_value = UNITS[to_]

    if unit_from_value.unit_name == unit_to_value.unit_name:
        x = value * unit_from_value.quantity / unit_to_value.quantity
    else:
        applied_value = value * unit_from_value.quantity
        value_in_result_units = applied_value / UNITS[unit_to_value.unit_name].quantity
        x = value_in_result_units / unit_to_value.quantity

    return x


def main():
    in_ = input()
    input_string = input_pattern.fullmatch(in_)

    if not input_string:
        sys.exit()

    quantity_from = float(input_string.group('quantity'))
    unit_from = input_string.group('unit_from')
    unit_to = input_string.group('unit_to')

    x = convert(quantity_from, unit_from, unit_to)

    print("{:.2e}".format(x))


if __name__ == '__main__':
    while True:
        try:
            main()
        except EOFError:
            sys.exit(0)
