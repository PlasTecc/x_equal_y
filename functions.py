from random import randint
from itertools import permutations
from string import digits
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


def check_expressions(expressions: list) -> bool:
    for expression in expressions:
        try:
            if eval(expression) == ANSWER:
                return True
        except ZeroDivisionError:
            continue
        except SyntaxError:
            continue
    return False


def generate_level() -> str:
    while True:
        random_numbers = generate_numbers()
        number_permutations = set(permutations(random_numbers))
        permutation: tuple[int, int, int, int]
        for permutation in number_permutations:
            expressions_list = get_expressions(permutation)
            if check_expressions(expressions_list):
                return "".join(map(str, random_numbers))


def validate_input(user_input: str, numbers: str) -> bool:
    digits_count = sum(c.isdigit() for c in user_input)
    signs_count = len([c for c in user_input if c in ["+", "-", "*", "/"]])
    if digits_count == NUMBERS_GIVEN and signs_count == NUMBERS_GIVEN - 1:
        for digit in digits:
            if user_input.count(digit) != numbers.count(digit):
                return False
        return eval(user_input) == ANSWER
    return False


def save_changes(numbers: str):
    if DATA['numbers'] is None:
        DATA['numbers'] = numbers
    with open(DATA_PATH, "w") as data_file:
        dump(DATA, data_file)


def clear_terminal():
    system("cls||clear")
