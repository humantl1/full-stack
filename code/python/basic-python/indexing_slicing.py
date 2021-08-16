#subscriptable: accessible by index
lst = ['zero', 'one', 'two', 'three', 'four']

print(lst[0:3]) #inclusive/exclusive pattern, colon = sliceable
print(lst[1::])
print(lst[-2::])

string = "hello" #strings also subscriptable
print(string[-2::])