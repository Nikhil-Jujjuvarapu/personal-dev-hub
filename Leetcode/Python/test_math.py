# test_math_functions.py
from math_fun import add

def test_add():
    assert add(2, 3) == 6      # This test should pass
    assert add(-1, 1) == -1    # Another passing test
    assert add(0, 0) == 0      # Edge case test
