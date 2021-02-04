name ="tome"
a =1
def fun():
    print(f"func {name}")
    global a
    a=2
    print(a)
    return None #默认会有这个


fun()
print("----")
print(a)
print(fun())