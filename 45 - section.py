
def accumulator():
    # import pdb; pdb.set_trace()
    total = 0
    value = None

    while True:
        value = yield total
        if value is None: break
        total += value


g1 = accumulator()
print(next(g1))
print(g1.send(1))
print(g1.send(10))
print(g1.send(100))
next(g1)