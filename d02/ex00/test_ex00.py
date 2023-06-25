import pytest
from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce
from functools import reduce

test_data = [
    ([i for i in range(10)], int),
    (tuple([i for i in range(10)]), int),
    ({i for i in range(10)}, int),
    ("Hello, world!", str),
    (b"Hello, world!", bytes),
    (range(10), int),
    ([i/10 for i in range(10)], float),
    ([i%2==0 for i in range(10)], bool),
    ([None for _ in range(10)], type(None)),
    (list("abcdefg"), str),
    (tuple("abcdefg"), str),
    (set("abcdefg"), str),
    ((True, False, True, False, True), bool),
    ({True, False}, bool),
    ((None, None, None, None, None), type(None)),
    (set([None]), type(None)),
    (range(-5, 5), int),
    ([i/3 for i in range(-10, 10)], float),
    (list(range(100, 200)), int),
    (tuple(range(100, 200)), int),
    (set(range(100, 200)), int),
    ("This is a longer string with more variety!", str),
    (b"This is a longer string with more variety!", bytes),
    (range(100, 200), int),
    ([i/100 for i in range(100, 200)], float),
    ([i%2==0 for i in range(100, 200)], bool),
    ([None for _ in range(100)], type(None)),
    (list("This is another string"), str),
    (tuple("This is another string"), str),
    (set("This is another string"), str),
    ([i%3==0 for i in range(100, 200)], bool),
    ((None,)*100, type(None)),
    (range(-100, 100), int),
    ([i/200 for i in range(-100, 100)], float),
]

test_functions = [
    (lambda x: x + 1, int),
    (lambda x: x * 2, int),
    (lambda x: x * x, int),
    (lambda x: x - 1, int),
    (lambda x: x * 3, int),
    (lambda x: x ** 2, int),
    (lambda x: x - 2, int),
    (lambda x: x * 4, int),
    (lambda x: x ** 3, int),
    (lambda x: x if x else 2, int),
    (lambda x: x if x else 1, int),
    (lambda x: x if x else 0, int),
    (lambda x: x if x else 'another default', str),
    (lambda x: x if x else 'default', str),
    (lambda x: x.upper(), str),
    (lambda x: x if x else '', str),
    (lambda x: x.lower(), str),
    (lambda x: not x, bool),
    (lambda x: x and x, bool),
    (lambda x: x or not x, bool),
    (lambda x: x and not x, bool),
    (lambda x: x or not x, bool),
    (lambda x: x in [10, 20, 30], bool),
    (lambda x: x not in [10, 20, 30], bool),
    (lambda x: x in [100, 200, 300], bool),
    (lambda x: x not in [100, 200, 300], bool),
    (lambda x: x and x, bool),
    (lambda x: x or x, bool),
    (lambda x: x is None, bool),
    (lambda x: x is not None, bool),
    (lambda x: x in [1, 2, 3], bool),
    (lambda x: x not in [1, 2, 3], bool),
    (lambda x: x / 3, float),
    (lambda x: x ** 0.5, float),
    (lambda x: x / 4, float),
    (lambda x: x / 2, float),
    (lambda x: x ** (1/3), float),
]

test_functions_reduce = [
    (lambda x, y: x + y, int),
    (lambda x, y: x - y, int),
    (lambda x, y: x * y, int),
    (lambda x, y: x / y if y != 0 else 1, float),
    (lambda x, y: x and y, bool),
    (lambda x, y: x or y, bool),
    (lambda x, y: x if x else y, int),
    (lambda x, y: x if x else y, str),
    (lambda x, y: x % y if y != 0 else 1, int),
    (lambda x, y: x // y if y != 0 else 1, int),
    (lambda x, y: (x + y) / 2, float),
    (lambda x, y: x if x > y else y, int),
    (lambda x, y: x if x < y else y, int),
    (lambda x, y: x ^ y, int),
    (lambda x, y: x & y, int),
    (lambda x, y: x | y, int),
    (lambda x, y: x if x else y, bool),
    (lambda x, y: x if not x else y, bool),
    (lambda x, y: x + y, str),
]

@pytest.mark.parametrize("data, data_type", test_data)
@pytest.mark.parametrize("func, func_return_type", test_functions)
def test_ft_map(data, data_type, func, func_return_type):
    if data_type == func_return_type:
        result = list(ft_map(func, data))
        expected = list(map(func, data))
        assert result == expected

@pytest.mark.parametrize("data, data_type", test_data)
@pytest.mark.parametrize("func, func_return_type", test_functions)
def test_ft_filter(data, data_type, func, func_return_type):
    if data_type == func_return_type:
        result = list(ft_filter(func, data))
        expected = list(filter(func, data))
        assert result == expected

@pytest.mark.parametrize("data, data_type", test_data)
@pytest.mark.parametrize("func, func_return_type", test_functions_reduce)
def test_ft_reduce(data, data_type, func, func_return_type):
    if data_type == func_return_type:
        result = ft_reduce(func, data)
        expected = reduce(func, data)
        assert result == expected

def test_non_iterable_input():
    non_iterables = [123, 456.789, True, None]
    for non_iterable in non_iterables:
        assert ft_map(lambda x: x, non_iterable) is None
        assert ft_filter(lambda x: x, non_iterable) is None
        assert ft_reduce(lambda x, y: x, non_iterable) is None

def test_non_function_input():
    non_functions = [123, 456.789, True, None, [1, 2, 3], (4, 5, 6), {7, 8, 9}]
    for non_function in non_functions:
        with pytest.raises(TypeError):
            list(ft_map(non_function, [1, 2, 3]))
            list(ft_filter(non_function, [1, 2, 3]))
            ft_reduce(non_function, [1, 2, 3])
