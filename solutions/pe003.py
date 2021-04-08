"""Project Euler - Solution to
Problem 3: Largest prime factor
https://projecteuler.net/problem=3

Solved by Jorge Espinoza
https://github.com/espinoza/project-euler
"""

def largest_prime_factor(number: int) -> int:
    if number < 2:
        return None
    factor = 1
    while factor < number:
        factor += 1
        while number % factor == 0:
            number /= factor
    return factor

print(largest_prime_factor(600851475143))