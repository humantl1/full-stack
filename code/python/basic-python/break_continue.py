items = ['one', 'two', 'three', 'four']

#continue starts next iteration of loop
for i in items:
    if i == 'two' or i == 'four':
        continue
    print(i)

for i in items:
    if i == 'three':
        break
    print(i)
