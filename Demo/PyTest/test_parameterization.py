import pytest


def sum(a, b):
    return a + b


@pytest.mark.parametrize("input1, input2, output", [
    (2, 3, 5),
    (3, 3, 6),
    (7, 3, 10),
    (11, 22, 33)
])
def test_calc_sum_1(input1, input2, output):
    result = sum(input1, input2)
    assert result == output


# def test_calc_sum_2():
#     result = sum(3, 3)
#     assert result == 6
#
#
# def test_calc_sum_3():
#     result = sum(7, 3)
#     assert result == 10

