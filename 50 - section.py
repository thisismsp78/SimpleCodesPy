class FooException(Exception):
    pass


# try:
#     raise FooException("insert description here")
# except FooException as e:
#     print("Foo exception is raised.")

class NegativeError(ValueError):
    pass


def foo(x):
    if x < 0:
        raise NegativeError("you entered negative error.")

