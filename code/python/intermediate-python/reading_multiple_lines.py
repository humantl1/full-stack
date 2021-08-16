
with open('example_text.txt', 'r') as example:
    txt = example.readlines() #store lines in list

print(txt)

print("Searching for the string 'next' in a line:")
for w in txt:
    if "next" in w:
        print(w.rstrip()) #rstrip removes trailing characters