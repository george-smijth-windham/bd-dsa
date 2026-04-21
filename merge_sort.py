def merge_sort(nums):
    # nums = [1,2]
    # print(f"nums: {nums}", f"left_side: {nums[:len(nums) // 2]}", f"right_side: {nums[len(nums) // 2:]}")
    # return []
    if len(nums) < 2:
        return nums
    left_side = merge_sort(nums[: len(nums) // 2])
    right_side = merge_sort(nums[len(nums) // 2 :])
    print(f"nums: {nums}", f"left_side: {left_side}", f"right_side: {right_side}")
    return merge(left_side, right_side)


def merge(left_side, right_side):
    return []
