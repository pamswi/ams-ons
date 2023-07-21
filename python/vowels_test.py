import pytest
from applications import vowels

def test_string():
    assert vowels.vowels("string") == 1