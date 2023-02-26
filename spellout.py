# -*- coding: utf-8 -*-

__author__ = 'ufian'

from typing import Any, Iterable, Tuple
from itertools import chain

MIN_NUMBER = 0
MAX_NUMBER = 10**12 - 1

GROUP_SIZE = 3
MIN_GROUP_NUMBER = 0
MAX_GROUP_NUMBER = 10**GROUP_SIZE - 1


HUNDRED = 100

CONSTANTS = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
}

GROUP_NAMES = [
    '', # 10**0
    'thousand' , # 10**3
    'million', # 10**6
    'billion', # 10**9
]


def _split_for_chunks(number: int) -> Iterable[int]:
    """
    Step 2: Split number into chunks of thousands in reverse order
    """
    if number < MIN_NUMBER or number > MAX_NUMBER:
        raise ValueError(f'Number must be between {MIN_NUMBER} and {MAX_NUMBER}')
    
    if number == 0:
        yield 0
        return
    
    while number > 0:
        yield number % 10**GROUP_SIZE
        number = number // 10**GROUP_SIZE

def _spellout_two_digits(number: int) -> str:
    """
    Step1: Spell out two-digit number.
    """
    if number < 0 or number >= HUNDRED:
        raise ValueError(f'Two digit number must be between 0 and f{HUNDRED - 1}')

    if number in CONSTANTS and number != HUNDRED:
        return CONSTANTS[number]

    tens = number // 10 * 10
    digit = number % 10
    
    return f'{CONSTANTS[tens]}-{CONSTANTS[digit]}'

def _spellout_hundreds(number_hundreds: int) -> str:
    if number_hundreds < 0 or number_hundreds > 9:
        raise ValueError('Number of hundreds must be between 0 and 9')
    
    if number_hundreds == 0:
        return ''
    
    return f'{CONSTANTS[number_hundreds]} {CONSTANTS[HUNDRED]}'
def _spellout_group(number: int) -> str:
    if number < MIN_GROUP_NUMBER or number > MAX_GROUP_NUMBER:
        raise ValueError(f'Number must be between {MIN_GROUP_NUMBER} and {MAX_GROUP_NUMBER}')
    
    # empty group
    if number == 0:
        return ''

    hundreds = number // HUNDRED
    two_digits = number % HUNDRED
    
    if two_digits == 0:
        return _spellout_hundreds(hundreds)
    
    parts = [
        _spellout_hundreds(hundreds),
        _spellout_two_digits(two_digits)
    ]
    
    return ' '.join(filter(lambda part: part != '', parts))

def spellout(number: int) -> str:
    """
    Convert an integer to its spelled-out form.
    """
    if number < MIN_NUMBER or number > MAX_NUMBER:
        raise ValueError(f'Number must be between {MIN_NUMBER} and {MAX_NUMBER}')
    
    # Edge case for zero
    if number == 0:
        return CONSTANTS[0]
    
    # zip for thousands chunks in reverse order and group names
    # Step 3 contains here
    reversed_groups = [
        (_spellout_group(group), group_name)
        for group, group_name in zip(_split_for_chunks(number), GROUP_NAMES)
        # filter empty groups
        if group != 0
    ]
    
    # Reverse to have correct order for output
    parts = chain.from_iterable(reversed(reversed_groups))
    return ' '.join(filter(None, parts))
