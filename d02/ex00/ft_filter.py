def ft_filter(function_to_apply, iterable):
    try:
        it = iter(iterable)
        return (x for x in it if function_to_apply(x))
    except (TypeError):
        return None
