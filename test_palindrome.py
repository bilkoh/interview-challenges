import pytest
from palindrome import palindrome


def test_simple_palindrome():
    assert palindrome("hannah")


def test_complex_palindrome():
    assert palindrome("Never odd, or even.")
