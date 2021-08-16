dictionary = {
    "key": "value",
    "bread": 2,
    5: "something"
}

dictionary["new key"] = "7.2"

print(dictionary[5], dictionary["key"])
print(dictionary)
del dictionary["bread"]
print(dictionary)