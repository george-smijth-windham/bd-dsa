def merge_sort(nums):
    if len(nums) < 2:
        return nums
    sorted_left_side = merge_sort(nums[: len(nums) // 2])
    sorted_right_side = merge_sort(nums[len(nums) // 2 :])
    return merge(sorted_left_side, sorted_right_side)


def merge(sorted_left_side, sorted_right_side):
    left_index, right_index = 0, 0
    sorted = []
    print(
        f"len_left: {len(sorted_left_side)}",
        f"sorted_left_side: {sorted_left_side}",
        f"len_right: {len(sorted_left_side)}",
        f"sorted_right_side: {sorted_right_side}",
        sep="\n",
    )
    while left_index < len(sorted_left_side) or right_index < len(sorted_right_side):
        if sorted_left_side[left_index] <= sorted_right_side[right_index]:
            print(
                f"left lt or eq right: {sorted_left_side[left_index]}, {sorted_right_side[right_index]}"
            )
            left_index += 1
        else:
            right_index += 1
    return sorted_left_side + sorted_right_side
