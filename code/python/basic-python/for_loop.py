#syntax: for element in iterable:

s = "string"
for l in s:
    print(l)

#dictionary by default prints keys
d = {
    "alpha": 1,
    "beta": 2,
    "gamma": 3
}
for k in d:
    print(k)

#to print key/val pair:
for k, v in d.items():
    print(f"[{k}: {v}]")