import pytest
from anagram import anagram


def test_simple_anagram():
    assert anagram("bored", "robed")


def test_complex_anagram():
    assert anagram("The Morse Code", "Here come dots")


def test_false_anagram():
    assert anagram("ABC", "XYZ") == False
