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

if __name__ == '__main__':
    print("\nConstruction from int value:")
    vec = Vector(42);
    print(vec)

    print("\nConstruction from range:")
    vec = Vector(range(1, 42, 2));
    print(vec)

    print("\nConstruction from column vector:")
    vec = Vector([[1.0], [2.0], [3.0], [4.0], [5.0], [6.0]]);
    print(vec)

    print("\nConstruction from row vector:")
    vec = Vector([[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]]);
    print(vec)

    print("\nWrong argument 'value' test:")
    try:
        vec = Vector("Hello world!");
        print("Input accepted: fail.")
    except ValueError:
        print("Error catched: success.")
    try:
        vec = Vector(1.0);
        print("Input accepted: fail.")
    except ValueError:
        print("Error catched: success.")
    try:
        vec = Vector([1.0, 2.0]);
        print("Input accepted: fail.")
    except ValueError:
        print("Error catched: success.")
    try:
        vec = Vector([1, 2]);
        print("Input accepted: fail.")
    except ValueError:
        print("Error catched: success.")
    try:
        vec = Vector([[1, 2]]);
        print("Input accepted: fail.")
    except ValueError:
        print("Error catched: success.")
    try:
        vec = Vector([[1], [2]]);
        print("Input accepted: fail.")
    except ValueError:
        print("Error catched: success.")
    try:
        vec = Vector([["Hello"], ["world!"]]);
        print("Input accepted: fail.")
    except ValueError:
        print("Error catched: success.")
    try:
        vec = Vector([["Hello", "world!"]]);
        print("Input accepted: fail.")
    except ValueError:
        print("Error catched: success.")

    print("\n__add__ test on row vector:")
    vec1 = Vector([[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]])
    vec2 = Vector([[9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0]])
    print(vec1 + vec2)

    print("\n__add__ test on column vector:")
    vec1 = Vector([[1.0], [2.0], [3.0], [4.0], [5.0], [6.0], [7.0], [8.0], [9.0]])
    vec2 = Vector([[9.0], [8.0], [7.0], [6.0], [5.0], [4.0], [3.0], [2.0], [1.0]])
    print(vec1 + vec2)

    print("\n__sub__ test on row vector:")
    vec1 = Vector([[42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0]])
    vec2 = Vector([[42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0]])
    print(vec1 - vec2)

    print("\n__sub__ test on column vector:")
    vec1 = Vector([[42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0]])
    vec2 = Vector([[42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0]])
    print(vec1 - vec2)

    print("\n__truediv__ test on row vector:")
    vec = Vector([[42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0]])
    print(vec / 1)

    print("\n__truediv__ test on column vector:")
    vec = Vector([[42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0]])
    print(vec / 1)

    print("\n__mul__ test on row vector:")
    vec = Vector([[42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0]])
    print(vec * 42)

    print("\n__mul__ test on column vector:")
    vec = Vector([[42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0]])
    print(vec * 42)

    print()
