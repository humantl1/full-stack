#syntax:
# def function_name(var1, var2):
# return "something"

def print_hello(name="Bob"): #any variable before a default is req'd
    print(f"Hello {name}!")
    return True

print_hello("you")