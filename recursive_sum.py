def recursive_sum_list(numbers):
    return 0 if len(numbers) == 0 else numbers[0] + recursive_sum_list(numbers[1:])


def recursive_sum_n(n):
    return 0 if n <= 0 else n + recursive_sum_n(n - 1)
