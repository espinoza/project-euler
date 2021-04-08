"""Project Euler - Solution to
Problem 2: Even Fibonacci numbers
https://projecteuler.net/problem=2

Solved by Jorge Espinoza
https://github.com/espinoza/project-euler
"""

from typing import Tuple


def sum_fibonacci_numbers(upper_bound: int, start_position: int = 1,
                          step: int = 1) -> int:
    amount = 0
    fibonacci_trio = (1, 2, 3)
    position = 1

    while position < start_position:
        fibonacci_trio = next_fibonacci_trio(fibonacci_trio)
        position += 1

    while fibonacci_trio[0] <= upper_bound:
        amount += fibonacci_trio[0]
        for i in range(step):
            fibonacci_trio = next_fibonacci_trio(fibonacci_trio)
            position += 1

    return amount


def next_fibonacci_trio(fib_trio: Tuple[int]) -> int:
    return (fib_trio[1], fib_trio[2], fib_trio[1] + fib_trio[2])


def sum_even_fibonacci_numbers(upper_bound: int) -> int:
    return sum_fibonacci_numbers(upper_bound, 2, 3)


print(sum_even_fibonacci_numbers(4000000))