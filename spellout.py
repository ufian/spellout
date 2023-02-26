# -*- coding: utf-8 -*-

__author__ = 'ufian'

from typing import Iterable
from itertools import chain

MIN_NUMBER = 0
MAX_NUMBER = 10**12 - 1

CHUNK_SIZE = 3
MIN_CHUNK_NUMBER = 0
MAX_CHUNK_NUMBER = 10**CHUNK_SIZE - 1

CHUNK_NAMES = [
    '', # 10**0
    'thousand', # 10**3
    'million', # 10**6
    'billion', # 10**9
]

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
        yield number % 10**CHUNK_SIZE
        number = number // 10**CHUNK_SIZE

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

def _spellout_chunk(number: int) -> str:
    if number < MIN_CHUNK_NUMBER or number > MAX_CHUNK_NUMBER:
        raise ValueError(f'Chunk must be between {MIN_CHUNK_NUMBER} and {MAX_CHUNK_NUMBER}')
    
    hundreds = number // HUNDRED
    two_digits = number % HUNDRED
    
    if two_digits == 0:
        return _spellout_hundreds(hundreds)
    
    parts = [
        _spellout_hundreds(hundreds),
        _spellout_two_digits(two_digits)
    ]
    
    return ' '.join(filter(None, parts))

def spellout(number: int) -> str:
    """
    Convert an integer to its spelled-out form.
    """
    if number < MIN_NUMBER or number > MAX_NUMBER:
        raise ValueError(f'Number must be between {MIN_NUMBER} and {MAX_NUMBER}')
    
    # Step 2: Split number into chunks of thousands in reverse order
    reversed_chunks = _split_for_chunks(number)
    
    # Step 3 map chunks to chunk names
    reversed_chunks_with_names = zip(reversed_chunks, CHUNK_NAMES)
    
    # filter empty chunks
    non_empty_lambda = lambda pair: pair[0] != 0
    reversed_chunks_with_names = filter(non_empty_lambda, reversed_chunks_with_names)

    # spell out chunks
    spellout_lambda = lambda pair: (_spellout_chunk(pair[0]), pair[1])
    reversed_chunks_with_names = map(spellout_lambda, reversed_chunks_with_names)
    
    # Reverse to have correct order for output
    parts = chain.from_iterable(reversed(list(reversed_chunks_with_names)))
    
    # filter empty tokens or return zero, if all tokens were empty
    return ' '.join(filter(None, parts)) or _spellout_two_digits(0)
