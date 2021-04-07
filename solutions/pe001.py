"""Project Euler - Solution to
Problem 1: Multiples of 3 and 5
https://projecteuler.net/problem=1

Solved by Jorge Espinoza
https://github.com/espinoza/project-euler
"""

def least_common_multiple(number1: int, number2: int) -> int:
    min_number = min(number1, number2)
    max_number = max(number1, number2)
    lcm = max_number
    while lcm % min_number > 0:
        lcm += max_number
    return lcm

def sum_multiples_of_a_number(number: int, supremum: int) -> int:
    factors_supremum = (supremum-1) // number
    return sum(number * i for i in range(1, factors_supremum+1))

def sum_multiples_of_two_numbers(number1: int, number2: int,
                                 supremum: int) -> int:
    sum1 = sum_multiples_of_a_number(number1, supremum)
    sum2 = sum_multiples_of_a_number(number2, supremum)
    lcm = least_common_multiple(number1, number2)
    sum_lcm = sum_multiples_of_a_number(lcm, supremum)
    return sum1 + sum2 - sum_lcm

print(sum_multiples_of_two_numbers(3, 5, 1000))