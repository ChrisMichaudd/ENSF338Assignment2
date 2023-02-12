import timeit
import matplotlib.pyplot as plt

def fib_original(n):
    if n <= 1:
        return n
    else:
        return fib_original(n-1) + fib_original(n-2)

cache = {}
def fib_memoized(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    result = fib_memoized(n-1) + fib_memoized(n-2)
    cache[n] = result
    return result

n_values = list(range(36))
times_original = []
times_memoized = []
for n in n_values:
    t_original = timeit.timeit('fib_original(' + str(n) + ')', setup='from __main__ import fib_original', number=10)
    times_original.append(t_original)

    t_memoized = timeit.timeit('fib_memoized(' + str(n) + ')', setup='from __main__ import fib_memoized', number=10)
    times_memoized.append(t_memoized)

plt.plot(n_values, times_original, label='Original')
plt.plot(n_values, times_memoized, label='Memoized')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Performance of Fibonacci Functions')
plt.legend()
plt.show()
