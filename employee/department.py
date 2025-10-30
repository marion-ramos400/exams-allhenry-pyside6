from enum import Enum
from random import choice

departments = [
    "IT",
    "HR",
    "Operations",
    "Administration",
    "Finance"
]

def randomDept():
    return choice(departments)
