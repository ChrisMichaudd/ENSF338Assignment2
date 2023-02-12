cache = {}

def fib(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    result = fib(n-1) + fib(n-2)
    cache[n] = result
    return result