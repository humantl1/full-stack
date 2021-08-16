#one way to create dictionary from list:
person = [("name", "Tim"), ("age", "38")]
d = {}
for key, value in person:
    d[key] = value
print(d)
print(type(d))

# dictionary comprehension way
dc = {key: value for key, value in person}
print(dc)

# really really short conversion
dc_short = dict(person)
print(dc_short)