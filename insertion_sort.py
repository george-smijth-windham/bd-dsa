def insertion_sort(nums):
    i = 0
    while i < len(nums):
        j = i
        while j > 0:
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
        i += 1
    return nums
