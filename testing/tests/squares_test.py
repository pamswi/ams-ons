import pytest
from applications import list_of_squares

def test_squares():
    assert list_of_squares.list_of_squares(2) == {1:1, 2:4}