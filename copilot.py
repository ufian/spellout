# -*- coding: utf-8 -*-


def spellout(number):
    if number < 0:
        return "minus " + spellout(-number)
    elif number < 20:
        return ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
                "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"][number]
    elif number < 100:
        return ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"][number // 10 - 2] + (
            " " + spellout(number % 10) if number % 10 else "")
    elif number < 1000:
        return spellout(number // 100) + " hundred" + (
            " " + spellout(number % 100) if number % 100 else "")
    elif number < 1000000:
        return spellout(number // 1000) + " thousand" + (
            " " + spellout(number % 1000) if number % 1000 else "")
    elif number < 1000000000:
        return spellout(number // 1000000) + " million" + (
            " " + spellout(number % 1000000) if number % 1000000 else "")
    elif number < 1000000000000:
        return spellout(number // 1000000000) + " billion" + (
            " " + spellout(number % 1000000000) if number % 1000000000 else "")
    elif number < 1000000000000000:
        return spellout(number // 1000000000000) + " trillion" + (
            " " + spellout(number % 1000000000000) if number % 1000000000000 else "")
    elif number < 1000000000000000000:
        return spellout(number // 1000000000000000) + " quadrillion" + (
            " " + spellout(number % 1000000000000000) if number % 1000000000000000 else "")
    elif number < 1000000000000000000000:
        return spellout
    