import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(10, 6) == 5
    assert calculator.fun1(8,1) == 5
    assert calculator.fun1 (-1, 1) == 0
    assert calculator.fun1 (-1, -1) == -2


def test_fun2():
    assert calculator.fun2(8, 9) == -1
    assert calculator.fun2(4,0) == 5
    assert calculator.fun2 (-3, 6) == -2
    assert calculator.fun2 (-8, -9) == 0

def test_fun3():
    assert calculator.fun3(5, 7) == 6
    assert calculator.fun3(9,0) == 0
    assert calculator.fun3 (-4, 6) == -1
    
    assert calculator.fun3 (-1, -1) == 1

def test_fun4():
    assert calculator.fun4(1, 3, 2) == 10
    assert calculator.fun4(3,1, -9) == 4
    assert calculator.fun4 (-2, -5, -8) == -3
    
    assert calculator.fun4 (-3, -2, 50) == 98
    
