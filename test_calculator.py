import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    """Тест сложения"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(2.5, 2.5) == 5.0

def test_subtract():
    """Тест вычитания"""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(10, 10) == 0

def test_multiply():
    """Тест умножения"""
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6
    assert multiply(2.5, 2) == 5.0

def test_divide():
    """Тест деления"""
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    assert divide(0, 5) == 0
    
def test_divide_by_zero():
    """Тест деления на ноль"""
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(5, 0)