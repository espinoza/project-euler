"""Project Euler - Solution to
Problem 4: Largest palindrome product
https://projecteuler.net/problem=4

Solved by Jorge Espinoza
https://github.com/espinoza/project-euler
"""

def count_digits(number: int) -> int:
    digits = 1
    while number >=10:
        number /= 10
        digits += 1
    return digits


def is_palindrome(number: int) -> bool:
    if count_digits(number) == 1:
        return True

    number_of_digits = count_digits(number)
    left_digit, remainder = divmod(number, 10 ** (number_of_digits - 1))
    middle, right_digit = divmod(remainder, 10)

    if left_digit == right_digit:
        new_number_of_digits = count_digits(middle)
        leading_zeros = number_of_digits - 2 - new_number_of_digits
        new_middle, must_be_zeros = divmod(middle, (10 ** leading_zeros))
        if must_be_zeros > 0:
            return False
        return is_palindrome(new_middle)

    return False


def largest_palindrome_product(number_of_digits_of_factors: int) -> int:
    largest_product = 1
    ndf = number_of_digits_of_factors
    min_factor = 10 ** (ndf - 1)
    max_factor = 10 ** ndf - 1

    middle_factor = min_factor
    while middle_factor <= max_factor:
        if int(middle_factor) == middle_factor:
            factor1 = int(middle_factor)
            factor2 = int(middle_factor)
        else:
            factor1 = int(middle_factor) + 1
            factor2 = int(middle_factor) - 1

        while factor1 <= max_factor and factor2 >= min_factor:
            product = factor1 * factor2
            if product > largest_product and is_palindrome(product):
                largest_product = product
            factor1 += 1
            factor2 -= 1

        middle_factor += 0.5

    return largest_product


print(largest_palindrome_product(3))


# Alternative solution

def largest_palindrome_product_v2(number_of_digits_of_factors: int) -> int:
    ndf = number_of_digits_of_factors
    factor_range = range(10 ** (ndf-1), 10 ** ndf)
    return max(x*y for x in factor_range for y in factor_range
               if str(x*y) == str(x*y)[::-1])

print(largest_palindrome_product_v2(3))