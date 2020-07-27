fib_map = {}


def fib(i):
    if i <= 1:
        return i
    if i in fib_map:
        return fib_map[i]
    else:
        tmp = fib(i - 1) + fib(i - 2)
        fib_map[i] = tmp
        return tmp


for n in range(100):
    print(fib(n))
