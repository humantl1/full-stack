# **kwargs argument is a dictionary, as opposed to the tupple of *args
def foo(**kwargs):
    print(kwargs)
    print(type(kwargs))

foo(one="a", two="b", three="c")