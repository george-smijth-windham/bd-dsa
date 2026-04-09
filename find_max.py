from functools import reduce


def find_max(nums):
    return reduce(lambda x, y: x if x > y else y, nums, float("-inf"))
