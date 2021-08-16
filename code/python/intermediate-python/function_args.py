# '*' before argument name denotes variable number of arguments (as tuple)
def foo(bar, *args):
    if bar:
        print(args)
    else:
        print("Nothing")

foo(False, 3, 2, 1)
foo(True, 1, 2, 3)