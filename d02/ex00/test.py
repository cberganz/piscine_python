from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce
import functools

def filter_test(elem):
    if elem > 4: return True
    else: return False

if __name__ == '__main__':

    # ft_map()
    print("\n1. ft_map()")

    print("\n1.1 Basic")
    it = [1, 2, 3, 4, 5, 6]
    for item in ft_map(lambda a: a*a, it):
        print(str(item) + ' ', end='')
    print()

    print("\n1.2 Error management")
    if ft_map(lambda a: a*a, None) is None: print("Success")
    else: print("KO")

    # ft_filter()
    print("\n2. ft_filter():")

    print("\n2.1 Basic")
    it = [1, 2, 3, 4, 5, 6]
    for item in ft_filter(filter_test, it):
        print(str(item) + ' ', end='')
    print()

    print("\n3. ft_filter():")
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
