def merge_sort(nums):
    if len(nums) < 2:
        return nums
    left = merge_sort(nums[: len(nums) // 2])
    right = merge_sort(nums[len(nums) // 2 :])
    print(f"left: {left}, right: {right}")
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    print(f"i: {i}, j: {j}")
    print(f"append left, left: {left}") if i < j else print(
        f"append right, right: {right}"
    )
    # result.append(left) if i < j else result.append(right)
    # result.extend(left[i:]) if i < j else result.extend(right[j:])
    # result + left[i:] if i < j else result + right[j:]
    # result = result + left[i:] if i < j else result + right[j]
    return result + left[i:] if i < j else result + right[j:]
