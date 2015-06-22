__author__ = 'Roman'

import math


def reduce(fn, coll):
    tmp = iter(coll)
    value = next(tmp)
    for v in tmp:
        value = fn(value, v)
    return value


def calculate_fractions(number: int):
    def is_fraction(n: int):
        return number % n == 0

    def divide(n: int):
        return int(number / n)

    tmp = list(filter(is_fraction, range(1, int(math.sqrt(number)) + 1)))

    return set(tmp + list(map(divide, tmp)))


def calc_mutual_fractions(*n: int):
    def intersect(x, y):
        return x & y

    return sorted(reduce(intersect, map(calculate_fractions, n)))


print(calc_mutual_fractions(128, 256))