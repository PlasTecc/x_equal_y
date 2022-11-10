from random import randint
from settings import *


def generate_numbers() -> tuple[int, ...]:
    return tuple([randint(0, 9) for _ in range(NUMBERS_GIVEN)])
