def countdown(n):
    return [] if n <= 0 else [n] + countdown(n - 1)
