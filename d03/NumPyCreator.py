import numpy as np

class NumpyCreator:
    def from_list(self, lst):
        """takes a list or nested lists and returns its corresponding Numpy array."""
        return np.array(lst, dtype=object)

    def from_tuple(self, tpl):
        """takes a tuple or nested tuples and returns its corresponding Numpy array."""
        return np.array(tpl, dtype=object)

    def from_iterable(self, itr):
        """takes an iterable and returns an array which contains all its elements."""
        return np.array(itr, dtype=object)

    #def from_shape(self, shape, value):
    #    """returns an array filled with the same value.
    #    The first argument is a tuple which specifies the shape of the array,
    #    and the second argument specifies the value of the elements.
    #    This value must be 0 by default."""
    #
    #def random(self, shape):
    #    """returns an array filled with random values. It takes as an argument
    #    a tuple which specifies the shape of the array."""
