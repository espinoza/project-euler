"""Project Euler - Solution to
Problem 7: 10001st prime
https://projecteuler.net/problem=7

Solved by Jorge Espinoza
https://github.com/espinoza/project-euler
"""

from typing import List


def is_prime(number: int, previous_prime_numbers: List[int]) -> bool:
    for prime in previous_prime_numbers:
        if number % prime == 0:
            return False
    return True


def find_prime_numbers(max_position: int) -> List[int]:
    prime_numbers = [2]
    position = 1
    number = 3
    while position < max_position:
        if is_prime(number, prime_numbers):
            prime_numbers.append(number)
            position += 1
        number += 2
    return prime_numbers


def nth_prime_number(position: int) -> int:
    return find_prime_numbers(position)[-1]
                
                
print(nth_prime_number(10001))