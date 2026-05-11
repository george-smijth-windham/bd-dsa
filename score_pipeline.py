from functools import reduce


def make_multiplier(factor):
    return lambda num: num * factor


def apply_pipeline(numbers, functions):
    return [reduce(lambda num, fn: fn(num), functions, num) for num in numbers]
    # if len(functions) == 0:
    #     return numbers
    # if len(numbers) == 0:
    #     return []
    # return [reduce(lambda x, y: y(x), functions, numbers[0])] + apply_pipeline(numbers[1:], functions)
    # print(functions)
    # return reduce(lambda x, y: y(x), functions, numbers[0]) + apply_pipeline(numbers[1:], functions)
