# content of test_sample.py
from main import *
# test_example.py
import pytest

@pytest.mark.parametrize("l1, l2, expected", [
    ("4", "1 2 3 4", 10),  # Тест-кейс 1
    ("7", "1000000 826 19 3 999997 1 100000", 2100846),# Тест-кейс 2

])
def test_addition(l1, l2, expected):

    assert mysum(l1,l2) == expected
