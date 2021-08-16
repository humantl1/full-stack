# if, for, while, and with do not create a scope
# there are 4 scopes in python:
# Local, Enclosing, Global, and Built-in. Variable scoping follows the LEGB rule

i = 0
while i < 10:
    i += 1
    j = 1

print(j)
