import pytest
from random import choice, randint
from string import ascii_letters, digits


def random_number(start: int = 1, end: int = 100) -> int:
    return randint(start, end)


def random_string(start: int = 6, end: int = 15) -> str:
    return ''.join(choice(ascii_letters + digits) for _ in range(randint(start, end)))


@pytest.fixture(scope="function")
def posts_data():
    return {
        'title': random_string,
        'body': random_string,
        'userId': random_number,
        'id': random_number
    }
