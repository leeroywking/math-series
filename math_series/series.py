def fibonacci(num: int) -> int:
    """
    recursive fibonacci function will break with values greater than 35 or so
    """
    return sum_series(num)

def fibonacci_iterative(num: int) -> int:
    """
    Iterative fibonacci function will work for much larger values
    """
    return sum_series_iterative(num)

def lucas(num: int) -> int:
    """
    recursive lucas function will break with values greater than 35 or so
    """
    return sum_series(num, 2, 1)


def lucas_iterative(num: int) -> int:
    """
    Iterative lucas function will work for much larger values
    """
    return sum_series_iterative(num, 2, 1)


def sum_series(num:int, first = 0, second = 1) -> int:
    """
    sum series function will break with values greater than 35 or so
    """
    if num == 0:
        return first
    elif num == 1:
        return second
    else:
        return sum_series(num -1, first, second) + sum_series(num -2, first, second)


def sum_series_iterative(num: int, first = 0, second = 1) -> int:
    """
    Iterative lucas function will work for much larger values
    """
    count = 1
    current = second
    previous = first
    if num == 0:
        return 0
    if num == 0:
        return current
    while count < num:
        store = current
        current = current + previous
        previous = store
        count += 1

    return current