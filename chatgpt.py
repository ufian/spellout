# -*- coding: utf-8 -*-

def spellout(number):
    if not 0 <= number <= 999_999_999_999:
        raise ValueError("Number out of range")

    if number == 0:
        return "zero"

    # Single-digit and teen numbers
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
            "seventeen", "eighteen", "nineteen"]
    # Multiples of ten
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    def spell_small(number):
        if number < 20:
            return ones[number]
        elif number < 100:
            return tens[number // 10] + ("" if number % 10 == 0 else "-" + ones[number % 10])
        else:
            return ones[number // 100] + " hundred" + ("" if number % 100 == 0 else " " + spell_small(number % 100))

    # Split number into chunks of 1000
    chunks = []
    while number > 0:
        chunks.append(number % 1000)
        number //= 1000

    # Convert each chunk to words and add the scale word
    scales = ["", "thousand", "million", "billion", "trillion"]
    words = []
    for i, chunk in enumerate(chunks):
        if chunk != 0:
            words.insert(0, spell_small(chunk) + " " + scales[i])

    # Join the list of words with spaces
    
    # Remark: the original code added 2 extra space at the end of the string
    return " ".join(words).strip()