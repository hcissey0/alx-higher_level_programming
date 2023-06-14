#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    if roman_string is None:
        return 0
    roman_string += "      "
    res = 0
    for i in range(len(roman_string)):
        if roman_string[i] == 'I':
            if roman_string[i + 1] == 'V':
                res -= 1
            elif roman_string[i + 1] == 'X':
                res -= 1
            else:
                res += 1
        elif roman_string[i] == 'V':
            res += 5
        elif roman_string[i] == 'X':
            if roman_string[i + 1] == 'L':
                res -= 10
            elif roman_string[i + 1] == 'C':
                res -= 10
            else:
                res += 10
        elif roman_string[i] == 'L':
            res += 50
        elif roman_string[i] == 'C':
            if roman_string[i + 1] == 'D':
                res -= 100
            elif roman_string[i + 1] == 'M':
                res -= 100
            else:
                res += 100
        elif roman_string[i] == 'D':
            res += 500
        elif roman_string[i] == 'M':
            res += 1000
    return res
