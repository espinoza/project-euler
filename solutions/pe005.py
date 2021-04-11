"""Project Euler - Solution to
Problem 5: Smallest multiple
https://projecteuler.net/problem=5

Solved by Jorge Espinoza
https://github.com/espinoza/project-euler
"""

from typing import List


def common_prime_factorization(numbers: List[int]) -> List[int]:
    factors = []
    for number in numbers:
        quotient = number
        for factor in factors:
            if quotient % factor == 0:
                quotient //= factor
        if quotient > 1:
            factors.append(quotient)
    return factors


def multiply_all(numbers: List[int]) -> int:
    product = 1
    for number in numbers:
        product *= number
    return product


def least_common_multiple(numbers: List[int]) -> int:
    return multiply_all(common_prime_factorization(numbers))


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(least_common_multiple(numbers))