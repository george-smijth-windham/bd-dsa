nums = []


def find_minimum(nums):
    minimum = float("inf")
    if len(nums) == 0:
        return
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum


result = find_minimum(nums)

print(result)
