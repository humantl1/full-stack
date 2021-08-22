def my_generator():
    for num in range(50):
        yield num ** num

#just examples of how generator works
gen_nums = my_generator() #generator object
print(gen_nums)
print(list(gen_nums))

all_nums = list(my_generator()) #cast as generator
print(all_nums)

#print and dispose of previous calc
for num in my_generator():
    print(num)

print("***")

#generators "exhaust" their resources
var_gen = my_generator()
ls_nums = list(var_gen)
print(ls_nums)
print("***")
for num in var_gen: #exhausted
    print(num)

