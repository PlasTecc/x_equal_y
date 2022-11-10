from random import randint
from settings import *


def generate_numbers() -> tuple[int, ...]:
    return tuple([randint(0, 9) for _ in range(NUMBERS_GIVEN)])


def get_expressions(numbers: tuple[int, ...]) -> list:
    expressions = []
    for operators in OPERATORS_LIST:
        expression = ""
        number_index = 0
        operators_index = 0
        for i in range(len(numbers) + len(operators)):
            if i % 2 == 0:
                expression += str(numbers[number_index])
                number_index += 1
            else:
                expression += str(operators[operators_index])
                operators_index += 1
        expressions.append(expression)
    return expressions
