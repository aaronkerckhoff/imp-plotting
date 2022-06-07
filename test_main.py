from main import calculate_next_y


def test_calculate_next_y():
    assert calculate_next_y(1, 2, 3) == 5
    assert calculate_next_y(2, 2, 3) == 7
    assert calculate_next_y(3, 2, 3) == 9
    assert calculate_next_y(20, 1, 5) == 25
    assert calculate_next_y(20, 2, 3) == 43
    assert calculate_next_y(9, 1.5, 2) == 15.5
    assert calculate_next_y(10, 1.5, 1) == 16
    assert calculate_next_y(10, 2, 1.5) == 21.5
    assert calculate_next_y(10, 2.5, 2) == 27
    assert calculate_next_y(39, 2.5, 1.4) == 98.9
