def fib(n):
    current, last = 1, 0
    for i in range(n - 1):
        yield current
        current, last = current + last, current

    yield current
