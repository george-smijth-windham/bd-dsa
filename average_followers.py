from functools import reduce


def average_followers(nums):
    if 0 == len(nums):
        return
    return reduce(lambda x, y: x + y, nums) / len(nums)
