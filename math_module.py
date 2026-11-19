"""Математичний модуль для демонстрації модульного тестування."""


def factorial(n: int) -> int:
    """Повертає факторіал невід'ємного цілого числа n.

    Args:
        n: Невід'ємне ціле число.

    Returns:
        Факторіал числа n.

    Raises:
        TypeError: Якщо n не є цілим числом або є булевим значенням.
        ValueError: Якщо n є від'ємним числом.
    """
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("Аргумент n повинен бути цілим числом")
    if n < 0:
        raise ValueError("Факторіал визначений лише для невід'ємних чисел")

    result = 1
    for number in range(2, n + 1):
        result *= number
    return result
