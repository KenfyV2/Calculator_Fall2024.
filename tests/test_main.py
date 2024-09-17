''' My Calculator Test'''
import pytest # type: ignore
from app.main import addition, division, subtraction, multiplication

def test_addition():
    '''Addition funtion'''
    assert addition(1,1)  == 2

def test_subtraction():
    '''Subtraction funtion'''
    assert subtraction(1,1)  == 0

def test_multiplication():
    assert multiplication(2,2) == 4

def test_division():
    assert division(2,2) == 1

def test_division_by_zero_exception():
    '''Test division to see if i get the exception by zero'''
    with pytest.raises(ZeroDivisionError):
        division(10, 0)