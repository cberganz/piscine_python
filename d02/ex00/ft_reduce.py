def ft_reduce(function_to_apply, iterable):
    try:
        iterator = iter(iterable)
        value = next(iterator)
        for element in iterator:
            value = function_to_apply(value, element)
        return value
    except TypeError:
        return None
