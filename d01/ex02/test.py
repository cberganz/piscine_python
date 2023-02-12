from vector import Vector

if __name__ == '__main__':

    # Instanciation
    print("\n1. Instanciation")

    print("\n1.1 Construction from int value:")
    vec = Vector(42);
    print(vec)
    print(vec.shape)

    print("\n1.2 Construction from range:")
    vec = Vector(range(1, 42, 2));
    print(vec)
    print(vec.shape)

    print("\n1.3 Construction from column vector:")
    vec = Vector([[1.0], [2.0], [3.0], [4.0], [5.0], [6.0]]);
    print(vec)
    print(vec.shape)

    print("\n1.4 Construction from row vector:")
    vec = Vector([[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]]);
    print(vec)
    print(vec.shape)

    # __str__ / __repr__
    print("\n2. __str__ / __repr__")

    print("\n2.1 __str__")
    print(vec)

    print("\n2.2 __repr__")
    print("This test must be run from the CLI interpreter.")


    print("\n1.5 Wrong argument 'value' test:")
    try:
        vec = Vector("Hello world!");
        print("Input accepted: fail.")
    except TypeError as e:
        print("Error catched: success: " + str(e))
    try:
        vec = Vector(1.0);
        print("Input accepted: fail.")
    except TypeError as e:
        print("Error catched: success: " + str(e))
    try:
        vec = Vector(range(12, 10));
        print("Input accepted: fail.")
    except TypeError as e:
        print("Error catched: success: " + str(e))
    try:
        vec = Vector([1.0, 2.0]);
        print("Input accepted: fail.")
    except TypeError as e:
        print("Error catched: success: " + str(e))
    try:
        vec = Vector([1, 2]);
        print("Input accepted: fail.")
    except TypeError as e:
        print("Error catched: success: " + str(e))
    try:
        vec = Vector([[1, 2]]);
        print("Input accepted: fail.")
    except TypeError as e:
        print("Error catched: success: " + str(e))
    try:
        vec = Vector([[1], [2]]);
        print("Input accepted: fail.")
    except TypeError as e:
        print("Error catched: success: " + str(e))
    try:
        vec = Vector([["Hello"], ["world!"]]);
        print("Input accepted: fail.")
    except TypeError as e:
        print("Error catched: success: " + str(e))
    try:
        vec = Vector([["Hello", "world!"]]);
        print("Input accepted: fail.")
    except TypeError as e:
        print("Error catched: success: " + str(e))
    try:
        vec = Vector([[1.0, 1.2, "hey", 1.4]]);
        print("Input accepted: fail.")
    except TypeError as e:
        print("Error catched: success: " + str(e))
    try:
        vec = Vector([[1.1], ["world!"], [1.2]]);
        print("Input accepted: fail.")
    except TypeError as e:
        print("Error catched: success: " + str(e))

    print()


    # __add__ / __radd__
    print("\n2. __add__ / __radd__")

    print("\n2.1 __add__ test on row vector:")
    vec1 = Vector([[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]])
    vec2 = Vector([[9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0]])
    print(vec1 + vec2)

    print("\n2.2 __add__ test on column vector:")
    vec1 = Vector([[1.0], [2.0], [3.0], [4.0], [5.0], [6.0], [7.0], [8.0], [9.0]])
    vec2 = Vector([[9.0], [8.0], [7.0], [6.0], [5.0], [4.0], [3.0], [2.0], [1.0]])
    print(vec1 + vec2)

    print("\n2.3 __radd__ test on row vector:")
    vec1 = Vector([[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]])
    vec2 = Vector([[9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0]])
    print(vec2 + vec1)

    print("\n2.4 __radd__ test on column vector:")
    vec1 = Vector([[1.0], [2.0], [3.0], [4.0], [5.0], [6.0], [7.0], [8.0], [9.0]])
    vec2 = Vector([[9.0], [8.0], [7.0], [6.0], [5.0], [4.0], [3.0], [2.0], [1.0]])
    print(vec2 + vec1)

    print("\n2.5 __add__ / __radd__ Exception handling:")
    vec1 = Vector([[1.1], [1.2], [1.3]]);
    vec2 = Vector([[1.1], [1.2], [1.3], [1.4]]);
    vec3 = Vector([[2.1, 2.2, 2.3]]);
    vec4 = Vector([[2.1, 2.2, 2.3, 2.4]]);
    try:
        a = vec1 + vec3
        print("input accepted: fail.")
    except TypeError as e:
        print("error catched: success: " + str(e))
    try:
        a = vec1 + vec4
        print("input accepted: fail.")
    except TypeError as e:
        print("error catched: success: " + str(e))
    try:
        a = vec2 + vec3
        print("input accepted: fail.")
    except TypeError as e:
        print("error catched: success: " + str(e))
    try:
        a = vec2 + vec4
        print("input accepted: fail.")
    except TypeError as e:
        print("error catched: success: " + str(e))
    try:
        a = vec3 + vec1
        print("input accepted: fail.")
    except TypeError as e:
        print("error catched: success: " + str(e))
    try:
        a = vec4 + vec1
        print("input accepted: fail.")
    except TypeError as e:
        print("error catched: success: " + str(e))
    try:
        a = vec3 + vec2
        print("input accepted: fail.")
    except TypeError as e:
        print("error catched: success: " + str(e))
    try:
        a = vec4 + vec2
        print("input accepted: fail.")
    except TypeError as e:
        print("error catched: success: " + str(e))
    try:
        a = vec4 + 1.0
        print("input accepted: fail.")
    except NotImplementedError as e:
        print("error catched: success: " + str(e))
    try:
        a = vec1 + [[1.1], [1.2], [1.3]]
        print("input accepted: fail.")
    except NotImplementedError as e:
        print("Error catched: success: " + str(e))
    try:
        a = 1.0 + vec4
        print("input accepted: fail.")
    except NotImplementedError as e:
        print("error catched: success: " + str(e))
    try:
        a = [[1.1], [1.2], [1.3]] + vec1
        print("input accepted: fail.")
    except NotImplementedError as e:
        print("Error catched: success: " + str(e))


    # __sub__ / __rsub__
    print("\n3. __sub__ / __rsub__")

    print("\n3.1 __sub__ test on row vector:")
    vec1 = Vector([[42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0]])
    vec2 = Vector([[41.0, 41.0, 41.0, 41.0, 41.0, 41.0, 41.0, 41.0, 41.0]])
    print(vec1 - vec2)

    print("\n3.2 __sub__ test on column vector:")
    vec1 = Vector([[42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0]])
    vec2 = Vector([[41.0], [41.0], [41.0], [41.0], [41.0], [41.0], [41.0], [41.0], [41.0]])
    print(vec1 - vec2)

    print("\n3.2 __rsub__ test on row vector:")
    vec1 = Vector([[42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0]])
    vec2 = Vector([[41.0, 41.0, 41.0, 41.0, 41.0, 41.0, 41.0, 41.0, 41.0]])
    print(vec2 - vec1)

    print("\n3.3 __rsub__ test on column vector:")
    vec1 = Vector([[42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0]])
    vec2 = Vector([[41.0], [41.0], [41.0], [41.0], [41.0], [41.0], [41.0], [41.0], [41.0]])
    print(vec2 - vec1)

    print("\n3.5 __sub__ / __rsub__ Exception handling:")
    vec1 = Vector([[1.1], [1.2], [1.3]]);
    vec2 = Vector([[1.1], [1.2], [1.3], [1.4]]);
    vec3 = Vector([[2.1, 2.2, 2.3]]);
    vec4 = Vector([[2.1, 2.2, 2.3, 2.4]]);
    try:
        a = vec1 - vec3
        print("input accepted: fail.")
    except TypeError as e:
        print("error catched: success: " + str(e))
    try:
        a = vec1 - vec4
        print("input accepted: fail.")
    except TypeError as e:
        print("error catched: success: " + str(e))
    try:
        a = vec2 - vec3
        print("input accepted: fail.")
    except TypeError as e:
        print("error catched: success: " + str(e))
    try:
        a = vec2 - vec4
        print("input accepted: fail.")
    except TypeError as e:
        print("error catched: success: " + str(e))
    try:
        a = vec3 - vec1
        print("input accepted: fail.")
    except TypeError as e:
        print("error catched: success: " + str(e))
    try:
        a = vec4 - vec1
        print("input accepted: fail.")
    except TypeError as e:
        print("error catched: success: " + str(e))
    try:
        a = vec3 - vec2
        print("input accepted: fail.")
    except TypeError as e:
        print("error catched: success: " + str(e))
    try:
        a = vec4 - vec2
        print("input accepted: fail.")
    except TypeError as e:
        print("error catched: success: " + str(e))
    try:
        a = vec4 - 1.0
        print("input accepted: fail.")
    except NotImplementedError as e:
        print("error catched: success: " + str(e))
    try:
        a = vec1 - [[1.1], [1.2], [1.3]]
        print("input accepted: fail.")
    except NotImplementedError as e:
        print("Error catched: success: " + str(e))
    try:
        a = 1.0 - vec4
        print("input accepted: fail.")
    except NotImplementedError as e:
        print("error catched: success: " + str(e))
    try:
        a = [[1.1], [1.2], [1.3]] - vec1
        print("input accepted: fail.")
    except NotImplementedError as e:
        print("Error catched: success: " + str(e))

    print()


    # __sub__ / __rsub__
    print("\n4. __truediv__ / __rtruediv__")

    print("\n4.1 __truediv__ test on row vector:")
    vec = Vector([[42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0]])
    print(vec / 2)

    print("\n4.2 __truediv__ test on column vector:")
    vec = Vector([[42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0]])
    print(vec / 2)

    print("\n4.3 __rtruediv__ test on row vector:")
    vec = Vector([[42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0]])
    try:
        print(2 / vec)
        print("input accepted: fail.")
    except ArithmeticError as e:
        print("Error catched: success: " + str(e))

    print("\n4.4 __rtruediv__ test on column vector:")
    vec = Vector([[42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0]])
    try:
        print(2 / vec)
        print("input accepted: fail.")
    except ArithmeticError as e:
        print("Error catched: success: " + str(e))

    print("\n4.5 __truediv__ test on column vector with non scalar:")
    vec = Vector([[42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0]])
    try:
        print(vec / "Hello")
        print("input accepted: fail.")
    except NotImplementedError as e:
        print("Error catched: success: " + str(e))
    try:
        print(vec / vec)
        print("input accepted: fail.")
    except NotImplementedError as e:
        print("Error catched: success: " + str(e))

    print()


    # __mul__ / __rmul__
    print("\n5. __mul__ / __rmull__")

    print("\n5.1 __mul__ test on row vector:")
    vec = Vector([[42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0]])
    print(vec * 10)

    print("\n5.2 __mul__ test on column vector:")
    vec = Vector([[42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0]])
    print(vec * 10)

    print("\n5.3 __rmul__ test on row vector:")
    vec = Vector([[42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0]])
    print(10 * vec)

    print("\n5.4 __rmul__ test on column vector:")
    vec = Vector([[42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0]])
    print(10 * vec)

    print("\n5.5 __mul__ / __rmul__ Exception handling:")
    try:
        print(vec * vec)
        print("input accepted: fail.")
    except NotImplementedError as e:
        print("Error catched: success: " + str(e))
    try:
        print(vec * "Hello")
        print("input accepted: fail.")
    except NotImplementedError as e:
        print("Error catched: success: " + str(e))
    try:
        print("Hello" * vec)
        print("input accepted: fail.")
    except NotImplementedError as e:
        print("Error catched: success: " + str(e))

    print()

    # dot()
    print("\n6. dot()")

    print("\n6.1 dot() method on line Vector")
    vec1 = Vector([[42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0, 42.0]])
    vec2 = Vector([[10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]])
    print(vec1.dot(vec2))
    print(vec2.dot(vec1))

    print("\n6.2 dot() method on column Vector")
    vec1 = Vector([[42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0], [42.0]])
    vec2 = Vector([[10.0], [10.0], [10.0], [10.0], [10.0], [10.0], [10.0], [10.0], [10.0]])
    print(vec1.dot(vec2))
    print(vec2.dot(vec1))

    print("\n6.3 dot() method on Vector of shape (1, 1)")
    vec1 = Vector([[42.0]])
    vec2 = Vector([[10.0]])
    print(vec1.dot(vec2))
    print(vec2.dot(vec1))

    print("\n6.4 dot() Exception handling:")
    vec1 = Vector([[42.0], [42.0], [42.0], [42.0]])
    vec2 = Vector([[10.0], [10.0], [10.0]])
    vec3 = Vector([[42.0, 42.0, 42.0, 42.0]])
    vec4 = Vector([[10.0, 10.0, 10.0]])
    try:
        print(vec1.dot("Hello"))
        print("input accepted: fail.")
    except NotImplementedError as e:
        print("Error catched: success: " + str(e))
    try:
        print(vec1.dot(2.0))
        print("input accepted: fail.")
    except NotImplementedError as e:
        print("Error catched: success: " + str(e))
    try:
        print(vec1.dot(2))
        print("input accepted: fail.")
    except NotImplementedError as e:
        print("Error catched: success: " + str(e))
    try:
        print(vec1.dot(vec2))
        print("input accepted: fail.")
    except TypeError as e:
        print("Error catched: success: " + str(e))
    try:
        print(vec2.dot(vec1))
        print("input accepted: fail.")
    except TypeError as e:
        print("Error catched: success: " + str(e))
    try:
        print(vec1.dot(vec3))
        print("input accepted: fail.")
    except TypeError as e:
        print("Error catched: success: " + str(e))
    try:
        print(vec3.dot(vec1))
        print("input accepted: fail.")
    except TypeError as e:
        print("Error catched: success: " + str(e))
    try:
        print(vec3.dot(vec4))
        print("input accepted: fail.")
    except TypeError as e:
        print("Error catched: success: " + str(e))
    try:
        print(vec4.dot(vec3))
        print("input accepted: fail.")
    except TypeError as e:
        print("Error catched: success: " + str(e))

    # T()
    print("\n7. T()")
    vec1 = Vector([[42.0], [42.0], [42.0], [42.0]])
    vec2 = Vector([[42.0, 42.0, 42.0, 42.0]])

    print("\n7.1 T() method on line Vector")
    print(vec2.T())

    print("\n7.2 T() method on column Vector")
    print(vec1.T())

    print("\n7.3 T() method on Vector of shape(1, 1)")
    print(Vector([[1.0]]).T())

    print("\n7.4 T() method on line Vector before dot() call")
    print(vec2.T().dot(vec2.T()))

    print("\n7.5 T() method on column Vector before dot() call")
    print(vec1.T().dot(vec1.T()))

    print()
