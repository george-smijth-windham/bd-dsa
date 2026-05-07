from functools import reduce


def exponential_growth(n, factor, days):
    return reduce(lambda x, _: x + [x[-1] * factor], list(range(days)), [n])
    # growth = n
    # result = []
    # for _ in range(days):
    #     growth *= factor
    #     result.append(growth)
    # return [n] + result
