# Exception

try:
    a = 2 / 0
    print(a)
except ZeroDivisionError as e:
    print(e)
else:
    if True:
        pass
    else:
        pass

try:
    pass
except ValueError as identifier:
    pass
finally:
    pass


try:
    pass
except KeyError as identifier:
    pass
else:
    pass
finally:
    pass

