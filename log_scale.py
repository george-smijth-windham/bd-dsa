from math import log


def log_scale(data, base):
    return [log(num, base) for num in data]
