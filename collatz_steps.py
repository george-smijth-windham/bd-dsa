def collatz_steps(n):
    if n < 1:
        raise ValueError(f"'{n}' must be a positive integer")
    return (
        0
        if n == 1
        else collatz_steps((3 * n + 1) if (n % 2 != 0 and n > 1) else n / 2) + 1
    )
