from vector import Vector

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
