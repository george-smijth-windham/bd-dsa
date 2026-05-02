def recursive_transform(data, fn):
    if isinstance(data, int) and not isinstance(data, bool):
        return fn(data)

    # if isinstance(data, list) or isinstance(data, tuple):
    #     result = []
    #     for item in data:
    #         transformed = recursive_transform(item, fn)
    #         result.append(transformed)
    #     return result
    if isinstance(data, list):
        result = []
        for item in data:
            transformed = recursive_transform(item, fn)
            result.append(transformed)
        return result

    if isinstance(data, tuple):
        result = []
        for item in data:
            transformed = recursive_transform(item, fn)
            result.append(transformed)
        return tuple(result)

    if isinstance(data, dict):
        result = {}
        for key, value in data.items():
            # new_key = recursive_transform(key, fn)
            new_value = recursive_transform(value, fn)
            result[key] = new_value
        return result

    return data


def double_int(n):
    return n * 2
