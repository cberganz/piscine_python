def ft_map(function_to_apply, iterable):
    try:
        it = iter(iterable)
        return (function_to_apply(x) for x in it)
    except TypeError:
        return None
