def foob(x):
    yield from range(x*2)
    yield from range(2)

# print(list(foob(5)))

def nums():
    yield 1
    yield 2
    yield 3

g1 = nums()
print(next(g1))
print(next(g1))
print(next(g1))
# print(next(g1))


def fib(a = 0, b = 1):
    while True:
        yield a
        a, b = b, a + b


f = fib()

print(', '.join(str(next(f)) for _ in range(10)))
