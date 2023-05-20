#!/usr/bin/python3


""" Operations """


def minOperations(n):
    op = 0
    factor = 2

    while n > 1:
        if n % factor == 0:
            op += factor
            n //= factor
        else:
            factor += 1

    return op
