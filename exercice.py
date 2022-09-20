#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        return-1*number
    return number



def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    SPACE = ' '
    noms= ''
    for lettre in prefixes:
        noms += f'{lettre}{suffixe} '
    print(noms)
print(use_prefixes())








def prime_integer_summation() -> int:
    return 0


def factorial(number: int) -> int:
    return 0


def use_continue() -> None:
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    return []






#
# if __name__ == '__main__':
#     main()
