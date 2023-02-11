from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce
from math import sqrt
import functools

def filter_test(elem):
    if elem > 4: return True
    else: return False

if __name__ == '__main__':
    print("\nTest ft_map:")
    it = [1, 2, 3, 4, 5, 6]
    for item in ft_map(sqrt, it):
        print(item)
    print("\nTest ft_filter:")
    it = [1, 2, 3, 4, 5, 6]
    for item in ft_filter(filter_test, it):
        print(item)
    print("\nTest ft_filter:")
    it = [1, 2, 3, 4, 5, 6]
    print(ft_reduce(lambda a,b: a+b, it))
    print(functools.reduce(lambda a,b: a+b, it))

    print("\nTest from subject:")
    #Example 1:
    x = [1, 2, 3, 4, 5]
    print(ft_map(lambda dum: dum + 1, x))
    print(list(ft_map(lambda t: t + 1, x)))
    # Example 2:
    print(ft_filter(lambda dum: not (dum % 2), x))
    print(list(ft_filter(lambda dum: not (dum % 2), x)))
    # Example 3:
    lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    print(ft_reduce(lambda u, v: u + v, lst))
