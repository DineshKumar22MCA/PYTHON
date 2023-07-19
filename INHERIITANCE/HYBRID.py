class a:
    def fun(self):
        print("class a")
class b(a):
    def fun1(self):
        print("class b")
class c(a):
    def fun2(self):
        print("class c")
class d(b,c):
    def fun3(self):
        print("class d")
o=d()
o.fun()
o.fun1()
o.fun2()
o.fun3()