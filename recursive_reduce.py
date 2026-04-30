def recursive_reduce(values, fn, initial):
    return (
        initial
        if len(values) == 0
        else fn(values[0], recursive_reduce(values[1:], fn, initial))
    )
