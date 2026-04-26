def recursive_map(func, items):
    return [] if len(items) == 0 else [func(items[0])] + recursive_map(func, items[1:])
