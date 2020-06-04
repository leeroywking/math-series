from math_series.series import fibonacci
from math_series.series import fibonacci_iterative
from math_series.series import lucas
from math_series.series import sum_series
from math_series.series import sum_series_iterative


def test_fib_pass_1():
    assert fibonacci(1) == 1


def test_fib_fail_1():
    assert not fibonacci(1) == 2


def test_fib_pass_0():
    assert fibonacci(0) == 0


def test_fib_fail_0():
    assert not fibonacci(0) == 2


def test_fib_pass_5():
    assert fibonacci(5) == 5


def test_fib_fail_5():
    assert not fibonacci(5) == 2


def test_fib_pass_6():
    assert fibonacci(6) == 8


def test_fib_fail_6():
    assert not fibonacci(30) == 2


def test_fib_pass_100():
    assert fibonacci_iterative(100) == 354224848179261915075


lucas_series = [2, 1, 3, 4, 7, 11, 18, 29]
def test_lucas():
    assert lucas(0) == lucas_series[0]


def test_lucas2():
    assert lucas(6) == lucas_series[6]


def test_sum_series():
    assert sum_series(0) == 0


def test_sum_series2():
    assert sum_series(0, 2, 1) == 2


def test_sum_series3():
    assert sum_series(5) == 5


def test_sum_series4():
    assert sum_series(5, 2, 1) == 11

