x = 10;
print(type(x))      #int
print(type(str(x))) #string
print(type(int))    #type

lst = ['1', '2', '3', '1']
print(set(lst)) #you can temporarily typecast to a set!
print(lst)
lst = set(lst)
print(lst)
lst = tuple(lst)
print(lst)
