#easy data structure search "in"
#functionality in python seems similar to c++, etc, but very simplified syntax
lst = ['a', 'b', 'c']
if 'a' in lst:
    print("a is in list")
else:
    print("a is not in list")

#use case: qualify input
input_options = ('q', 's', 'n')
user_input = input("Enter option: ")
if user_input not in input_options:
    print("invalid option")
else:
    print("returning")