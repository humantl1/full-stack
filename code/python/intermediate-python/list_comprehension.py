# list comprehension: populate a list with an inline for loop
numbers = []
for num in [1, 2, 3, 4, 5, 6]:
    numbers.append(num**2)
print(numbers)

nums = [num**2 for num in [1, 2, 3, 4, 5]]
print(nums)

#online example of if statement in list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)