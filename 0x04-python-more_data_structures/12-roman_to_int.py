#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return None
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i, c in enumerate(roman_string):
        if (i + 1) == len(roman_string) or rom[c] >= rom[roman_string[i + 1]]:
            result += rom[c]
        else:
            result -= rom[c]
    return result
