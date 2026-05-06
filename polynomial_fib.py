def fib(n):
    if n <= 1:
        return n
    grandparent = 0
    parent = 1
    current = None
    for i in range(n - 1):
        current = parent + grandparent
        grandparent = parent
        parent = current
    return current
