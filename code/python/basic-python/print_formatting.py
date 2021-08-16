name = input("enter your name ")
format_message = "Hello {}!".format(name) #format function
fstring_message = f"Hello {name}!"
old_message = "Hello %s!" %name
print(format_message)
print(fstring_message)
print(old_message)
