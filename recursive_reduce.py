def recursive_reduce(values, fn, initial):
    return (
        initial
        if len(values) == 0
        else fn(values[0], recursive_reduce(values[1:], fn, initial))
    )


# a way to deal with missing initial
# _MISSING = object()

# def recursive_reduce(values, fn, initial=_MISSING):
# if initial is _MISSING:
# if len(values) == 0:
# raise ValueError("reduce of empty sequence with no initial value")
# if len(values) == 1:
# return values[0]
# proceed without initial...
# ...
