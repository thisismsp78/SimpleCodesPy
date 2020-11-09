import contextlib

@contextlib.contextmanager
def context_manager(num):
    print("Enter")
    try:
        yield num + 1
    except ZeroDivisionError as e:
        print("cauth error: {}".format(e))
    finally:
        print("Cleaning up")
    print("Exit")

with context_manager(2) as cm:

    print("Right in the middle with cm = {}".format(cm))


# 1. run statements before yield
# 1.1 run try
# 2. run statements in the body of the context_manager
# 2.1 if safe run finally
# 2.2 else run except
# 2.3 run finally
# 3. run statements after yield
