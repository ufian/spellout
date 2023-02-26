# -*- coding: utf-8 -*-

def spellout(number):
    """
    Convert an integer to its spelled-out form.
    """
    # Define dictionaries for the different number ranges
    ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
            5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
            6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
    teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
             14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
             18: 'eighteen', 19: 'nineteen'}
    thousands = {0: '', 1: 'thousand', 2: 'million', 3: 'billion',
                 4: 'trillion', 5: 'quadrillion', 6: 'quintillion',
                 7: 'sextillion', 8: 'septillion', 9: 'octillion'}

    # Handle negative numbers
    if number < 0:
        return "minus " + spellout(abs(number))

    # Handle zero and single-digit numbers
    if number < 10:
        return ones[number]

    # Handle two-digit numbers
    if number < 100:
        if number in teens:
            return teens[number]
        else:
            ten_digit = number // 10
            one_digit = number % 10
            if one_digit == 0:
                return tens[ten_digit]
            else:
                return tens[ten_digit] + '-' + ones[one_digit]

    # Handle three-digit numbers
    if number < 1000:
        hundred_digit = number // 100
        remainder = number % 100
        if remainder == 0:
            return ones[hundred_digit] + ' hundred'
        else:
            return ones[hundred_digit] + ' hundred and ' + spellout(remainder)

    # Handle larger numbers
    for i in range(1, len(thousands)):
        if number < 1000**(i+1):
            quotient = number // 1000**i
            remainder = number % 1000**i
            if quotient == 0:
                continue
            elif remainder == 0:
                return spellout(quotient) + ' ' + thousands[i]
            else:
                return spellout(quotient) + ' ' + thousands[i] + ', ' + spellout(remainder)

    # Handle numbers that are too large
    raise ValueError("Number out of range for spellout function.")