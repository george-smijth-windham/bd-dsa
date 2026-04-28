def recursive_sum(numbers):
    return 0 if len(numbers) == 0 else numbers[0] + recursive_sum(numbers[1:])


def recursive_sum_two(n):
    return 0 if n <= 0 else n + recursive_sum_two(n - 1)
