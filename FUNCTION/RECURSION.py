def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)
print(fact(4))

def fun():
    print("hello world")
    fun()
fun()
