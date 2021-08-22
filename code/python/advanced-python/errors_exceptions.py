try:
    total = 1 / 0
except Exception:
    total = None
    print("error: division by zero")
print(total)

num = input("Enter a number: ")
num2 = input("Enter a second number: ")
try:
    num = int(num)
    num2 = int(num2)
    total = num / num2
except ValueError:
    print("num or num2 is not a valid number")
    num = None
    num2 = None
except Exception as e:
    print("Exception was caught", type(e))
    num = None
    num2 = None
print("num =", num)
print("num2 =", num2)