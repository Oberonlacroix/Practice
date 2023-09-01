import calc

def test_addition():
    assert calc.addition(3, 4) == 7
    assert calc.addition(1000, 1) == 1001
    assert calc.addition(54, 45) == 99
    assert calc.addition(12, 16) == 28
    assert calc.addition(14, 20) == 34

def test_subtraction():
    assert calc.subtraction(8, 5) == 3
    assert calc.subtraction(15, 9) == 6
    assert calc.subtraction(25, 5) == 20
    assert calc.subtraction(80, 19) == 61
    assert calc.subtraction(54, 3) == 51

def test_division():
    assert calc.division(20, 4) == 5
    assert calc.division(80, 4) == 20
    assert calc.division(50, 10) == 5
    assert calc.division(100, 1) == 100
    assert calc.division(5, 1) == 5

def test_multiplication():
    assert calc.multiplication(15, 4) == 60
    assert calc.multiplication(3, 9) == 27
    assert calc.multiplication(5, 6) == 30
    assert calc.multiplication(19, 1) == 19
    assert calc.multiplication(12, 3) == 36

