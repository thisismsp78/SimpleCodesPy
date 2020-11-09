#Context Manager

class MyContextManager:
    def __enter__(self):
        print("Entered")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("exited" + (" (with an exception)" if exc_type else ""))
        # return True if you want to suppress the exception.

with MyContextManager() as a:
    print("a is {}".format(a))
    raise ValueError("My Error")
