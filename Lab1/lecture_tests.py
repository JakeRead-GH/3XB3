import timeit
import random
import matplotlib.pyplot as plot

def mean(L):
    return sum(L)/len(L)

def var(L):
    square_sum = 0
    for num in L:
        square_sum += num**2
    return abs(mean(L)**2 - square_sum/len(L))

def create_random_list(length, max_value):
    L = []
    for _ in range(length):
        L.append(random.randint(0, max_value))
    return L

def experiment0(n,m):
    time = 0
    for _ in range(m):
        L = create_random_list(n, n)
        start = timeit.default_timer()
        L2 = L.copy()
        end = timeit.default_timer()
        time += end - start
    return time/m

def experiment01(n, m, k):
    times = []
    for _ in range(k):
        times.append(experiment0(n, m))
    return times

def experiement1(n, m, step):
    times = []
    for i in range(0, n, step):
        time = 0
        for _ in range(m):
            L = create_random_list(i, i)
            start = timeit.default_timer()
            L2 = L.copy()
            end = timeit.default_timer()
            time += end - start
        times.append(time/m)
    return times


def experiement2(n, m):
    times = []
    L = create_random_list(n, n)
    for i in range(n):
        time = 0
        for _ in range(m):
            start = timeit.default_timer()
            x = L[i]
            end = timeit.default_timer()
            time += end - start
        times.append(time/m)
    return times


def experiement3(n):
    times = []
    L = []
    for i in range(n):
        time = 0
        start = timeit.default_timer()
        L.append(i)
        end = timeit.default_timer()
        times.append(end - start)
    return times

def experiement4(n):
    times = []
    for i in range(n):
        start = timeit.default_timer()
        fib(i)
        end = timeit.default_timer()
        times.append(end - start)
    return times

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

times = experiement3(10000000)
plot.plot(times)
plot.show()







"""
def experiement1():
    times = []
    for i in range(0, 100000, 1000):
        L = create_random_list(i, i)
        time = 0
        for _ in range(1):
            start = timeit.default_timer()
            L2 = L.copy()
            end = timeit.default_timer()
            time += end - start
        times.append(time/1)
        return times


def experiement2(n, m):
    times = []
    L = create_random_list(n, n)
    for i in range(n):
        time = 0
        for _ in range(m):
            start = timeit.default_timer()
            x = L[i]
            end = timeit.default_timer()
            time += end - start
        times.append(time/m)
    return times


def experiement3(n):
    times = []
    L = []
    for i in range(n):
        time = 0
        start = timeit.default_timer()
        L.append(i)
        end = timeit.default_timer()
        times.append(end - start)
    return times

def experiement4(n):
    times = []
    for i in range(n):
        start = timeit.default_timer()
        fib(i)
        end = timeit.default_timer()
        times.append(end - start)
    return times
"""