class stud:

    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        stud.count +=1
    def fun(self):
        print(self.name,self.age)
    @classmethod
    def fun2(cls):
        return stud.count

o=stud("virat",35)
o.fun()
print(stud.fun2())
o1=stud("dhoni",42)
o1.fun()
print(stud.fun2())
print(o.fun2())
print(stud.count)