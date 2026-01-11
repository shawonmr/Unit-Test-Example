# test_calculator.py
from calculator import add, subtract

def test_add_two_positives():
    """Test standard addition of two positive integers."""
    assert add(10, 5) == 15

def test_add_with_zero():
    """Test addition involving zero."""
    assert add(7, 0) == 7

def test_subtract_positive_from_negative():
    """Test subtraction to ensure a negative result is handled."""
    assert subtract(-5, 5) == -10

def test_subtract_error_example():
    """This test is designed to fail to show the pytest output."""
    assert subtract(10, 3) == 6  # Fails because 10 - 3 is 7, not 6
