import main
from pytest import approx


# Test the different calculations
def test_calculate_next_1():
    assert main.calculate_next_1(1) == 1
    assert main.calculate_next_1(2) == 4
    assert main.calculate_next_1(3) == 9
    assert main.calculate_next_1(3.5) == 12.25
    assert main.calculate_next_1(5.5) == 30.25


def test_calculate_next_2():
    assert main.calculate_next_2(1) == 1
    assert main.calculate_next_2(2) == 32
    assert main.calculate_next_2(3) == 243
    assert main.calculate_next_2(3.5) == 525.21875
    assert main.calculate_next_2(5.5) == 5032.84375


def test_calculate_next_3():
    assert main.calculate_next_3(1) == 1
    assert main.calculate_next_3(2) == approx(1.41421, 0.00001)
    assert main.calculate_next_3(3) == approx(1.73205, 0.00001)
    assert main.calculate_next_3(3.5) == approx(1.87083, 0.00001)
    assert main.calculate_next_3(5.5) == approx(2.34520, 0.00001)


def test_calculate_next_4():
    assert main.calculate_next_4(1) == -1
    assert main.calculate_next_4(2) == -32
    assert main.calculate_next_4(3) == -243
    assert main.calculate_next_4(3.5) == -525.21875
    assert main.calculate_next_4(5.5) == -5032.84375
