class user:
    @property
    def fun(self):
        print("hello world")
o=user()
print(o.fun)

class users:
    def __init__(self,n,a):
        self.name=n
        self.age=a
       # self.msg="name:",self.name,"age:",self.age
    @property
    def fun2(self):
        return "name:",self.name,"age:",self.age

o1=users("virat",35)
print(o1.name)
print(o1.age)
print(o1.fun2)
o1.age=25
print(o1.fun2)


