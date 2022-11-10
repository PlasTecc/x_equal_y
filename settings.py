from itertools import product
from os import path, getcwd
from json import dump, load

# Variables
ANSWER = 10
NUMBERS_GIVEN = 4
OPERATORS_LIST = list(product("+-*/", repeat=NUMBERS_GIVEN - 1))
DATA_PATH = path.join(getcwd(), "data.json")
DATA = {"score": 0}

# Initialize Score
if path.exists(DATA_PATH):
    with open(DATA_PATH, "r") as file:
        DATA = load(file)
else:
    with open(DATA_PATH, "w") as file:
        dump(DATA, file)
