# enumeration is a property of iterables
animals = ["Gully", "Rhubarb", "Zephyr", "Henry"]
for index, animal in enumerate(animals):
    if index % 2 == 0:
        continue
    print(animal)