# Generators

def myfunc():
    for x in range(10):
        yield x ** 2


g1 = myfunc()
g2 = (x ** 2 for x in range(10))

print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))