def recursive_map(func, items):
    return [] if len(items) == 0 else [func(items[0])] + recursive_map(func, items[1:])


def recursive_map_two(values, transform):
    if len(values) == 0:
        return []
    first = values[0]
    rest = values[1:]
    transformed = transform(first)
    return [transformed] + recursive_map_two(rest, transform)
