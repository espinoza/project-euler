"""Project Euler - Solution to
Problem 6: Sum square difference
https://projecteuler.net/problem=6

Solved by Jorge Espinoza
https://github.com/espinoza/project-euler
"""

def sum_of_the_squares(upper_bound: int) -> int:
    return sum(i ** 2 for i in range(1, upper_bound+1))

def square_of_the_sum(upper_bound: int) -> int:
    return sum(i for i in range(1, upper_bound+1)) ** 2

print(square_of_the_sum(100) - sum_of_the_squares(100))