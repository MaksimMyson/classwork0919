a = int(input("a: "))3
b = int(input("b: "))
if a != b and a < b:
    print(str(a) + " " + str(b))
elif a != b and a > b:
    print(str(b) + " " + str(a))
else:
    print("a = b")
