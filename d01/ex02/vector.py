import numpy

class Vector:
    def __init__(self, values):
        if isinstance(values, list) \
        and isinstance(values[0], list) \
        and isinstance(values[0][0], float):
            self.shape = (len(values), len(values[0]))
            self.values = values.copy()
        elif isinstance(values, int):
            self.values = [[i] for i in range(values)]
            self.shape = (len(self.values), 1)
        elif isinstance(values, range):
            self.values = [[i] for i in values]
            self.shape = (len(self.values), 1)
        else:
            raise ValueError("Error: Vector: __init__: Wrong argument: 'values'.")

    def __str__(self):
        return str(self.values)

    def __add__(self, oper):
        if not isinstance(oper, Vector) or self.shape != oper.shape:
            raise ValueError("Error: Vector: __add__: Wrong operation.")
        ret = []
        for i in range(len(self)):
            for j in range(len(self[0])):
                ret += [self[i][j] + oper[i][j]]
        return ret

    def __radd__(self, oper):
        return self + oper

    def __sub__(self, oper):
        if not isinstance(oper, Vector) or self.shape != oper.shape:
            raise ValueError("Error: Vector: __sub__: Wrong operation.")
        ret = []
        for i in range(len(self)):
            for j in range(len(self[0])):
                ret += [self[i][j] - oper[i][j]]
        return ret

    def __rsub__(self, oper):
        if not isinstance(oper, Vector) or self.shape != oper.shape:
            raise ValueError("Error: Vector: __rsub__: Wrong operation.")
        ret = []
        for i in range(len(self)):
            for j in range(len(self[0])):
                ret += [oper[i][j] - self[i][j]]
        return ret

    def __truediv__(self, scalar):
        if not numpy.isscalar(scalar):
            raise ValueError("Error: Vector: __truediv__: Wrong operation.")
        ret = []
        for i in range(len(self)):
            for j in range(len(self[0])):
                ret += [self[i][j] / scalar]
        return ret

    def __rtruediv__(self, scalar):
        raise ValueError("Division of a scalar by a Vector is not defined here.")


    def __mul__(self, scalar):
        if not numpy.isscalar(scalar):
            raise ValueError("Error: Vector: __mul__: Wrong operation.")
        ret = []
        for i in range(len(self)):
            for j in range(len(self[0])):
                ret += [self[i][j] * scalar]
        return ret

    def __rmul__(self, scalar):
        return self * scalar

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]
