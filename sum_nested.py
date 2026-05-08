from functools import reduce


def sum_nested(values):
    return (
        values
        if isinstance(values, int)
        else reduce(lambda x, y: x + sum_nested(y), values, 0)
    )
