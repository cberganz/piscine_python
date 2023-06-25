def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    try:
        it = iter(iterable)
        ret = next(it)
        for item in it:
            ret = function_to_apply(ret, item)
        return ret
    except:
        return None
