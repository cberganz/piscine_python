class Vector:
    def __init__(self, values):
        if isinstance(values, list) \
        and isinstance(values[0], list):
            for item in values:
                for number in item:
                    if not isinstance(number, float):
                        raise TypeError("Error: Vector: __init__: initializer list contains a non float value: '" + str(number) + "'.")
            self.shape = (len(values), len(values[0]))
            self.values = values.copy()
        elif isinstance(values, int):
            self.values = [[i] for i in range(values)]
            self.shape = (len(self.values), 1)
        elif isinstance(values, range):
            if values.start > values.stop:
                raise TypeError("Error: Vector: __init__: range argument: start > end.")
            self.values = [[i] for i in values]
            self.shape = (len(self.values), 1)
        else:
            raise TypeError("Error: Vector: __init__: Wrong argument: 'values'.")

    def dot(self, arg):
        if not isinstance(arg, Vector):
            raise NotImplementedError("Error: Vector: dot() with non Vector: Not implemented.")
        if self.shape != arg.shape:
            raise TypeError("Error: Vector: dot(): Vector shapes are different.")
        new = []
        for item in zip(self.values, arg.values):
            for number in zip(item[0], item[1]):
                new.append(number[0] * number[1] if self.shape[0] == 1 else [number[0] * number[1]])
        return Vector([new] if self.shape[0] == 1 else new)

    def T(self):
        new = []
        for item in self.values:
            for number in item:
                new.append([number] if self.shape[0] == 1 else number)
        return Vector(new if self.shape[0] == 1 else [new])

    def __str__(self):
        return str(self.values)

    def __add__(self, oper):
        if not isinstance(oper, Vector):
            raise NotImplementedError("Error: Vector: __add__ with non Vector: Not implemented.")
        if self.shape != oper.shape:
            raise TypeError("Error: Vector: __add__: Vector shapes are different.")
        ret = []
        for i in range(len(self)):
            for j in range(len(self[0])):
                ret += [self[i][j] + oper[i][j]]
        return ret

    def __radd__(self, oper):
        return self + oper

    def __sub__(self, oper):
        if not isinstance(oper, Vector):
            raise NotImplementedError("Error: Vector: __sub__ with non Vector: Not implemented.")
        if self.shape != oper.shape:
            raise TypeError("Error: Vector: __sub__: Vector shapes are different.")
        ret = []
        for i in range(len(self)):
            for j in range(len(self[0])):
                ret += [self[i][j] - oper[i][j]]
        return ret

    def __rsub__(self, oper):
        if not isinstance(oper, Vector):
            raise NotImplementedError("Error: Vector: __rsub__ with non Vector: Not implemented.")
        if self.shape != oper.shape:
            raise TypeError("Error: Vector: __rsub__: Vector shapes are different.")
        ret = []
        for i in range(len(self)):
            for j in range(len(self[0])):
                ret += [oper[i][j] - self[i][j]]
        return ret

    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise NotImplementedError("Error: Vector: __truediv__ with non scalar: Not implemented.")
        ret = []
        for i in range(len(self)):
            for j in range(len(self[0])):
                ret += [self[i][j] / scalar]
        return ret

    def __rtruediv__(self, scalar):
        raise ArithmeticError("Error: Vector: __rtruediv__: Division of a scalar by a Vector is not implemented.")


    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise NotImplementedError("Error: Vector: __mul__ with non scalar: Not implemented.")
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

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return str(self.values)
