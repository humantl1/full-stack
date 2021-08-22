def my_decorator(func):
    def wrapper():
        print("Do Something")
        func()
        print("Finish original function")
    return wrapper

@my_decorator
def myfunc():
    print("I'm Tim")

myfunc()