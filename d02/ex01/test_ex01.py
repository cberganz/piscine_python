import pytest

def what_are_the_vars(*args, **kwargs):
    obj = ObjectC()
    for index, item in enumerate(args):
        setattr(obj, "var_{}".format(index), item)
    for key, value in kwargs.items():
        if hasattr(obj, key):
            return None
        setattr(obj, key, value)
    return obj

class ObjectC(object):
    def __init__(self):
        pass

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")
    
def test_what_are_the_vars():
    obj = what_are_the_vars(7)
    assert obj.var_0 == 7

    obj = what_are_the_vars(None, [])
    assert obj.var_0 == None
    assert obj.var_1 == []

    obj = what_are_the_vars("ft_lol", "Hi")
    assert obj.var_0 == "ft_lol"
    assert obj.var_1 == "Hi"

    obj = what_are_the_vars()
    assert len(obj.__dict__) == 0

    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    assert obj.var_0 == 12
    assert obj.var_1 == "Yes"
    assert obj.var_2 == [0, 0, 0]
    assert obj.a == 10
    assert obj.hello == "world"

    obj = what_are_the_vars(42, a=10, var_0="world")
    assert obj is None

    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    assert obj.var_0 == 42
    assert obj.var_1 == "Yes"
    assert obj.a == 10
    assert obj.var_2 == "world"
