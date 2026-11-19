import pytest

from math_module import factorial


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (0, 1),
        (1, 1),
        (5, 120),
        (7, 5040),
        (10, 3628800),
    ],
)
def test_factorial_valid_inputs(number, expected):
    """Перевіряє факторіал для коректних вхідних значень."""
    assert factorial(number) == expected


def test_factorial_negative_number():
    """Для від'ємного числа має виникати ValueError."""
    with pytest.raises(ValueError, match="невід'ємних"):
        factorial(-3)


def test_factorial_non_integer_number():
    """Для дійсного числа має виникати TypeError."""
    with pytest.raises(TypeError, match="цілим числом"):
        factorial(3.5)


def test_factorial_boolean_value():
    """Булеві значення не повинні прийматися як цілі числа."""
    with pytest.raises(TypeError, match="цілим числом"):
        factorial(True)
