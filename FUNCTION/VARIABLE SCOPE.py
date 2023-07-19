
b=10
def fun(a):
    global b
    b=15

    print("hello",a)
    print(b)


fun(5)
print(b)
#print(a)