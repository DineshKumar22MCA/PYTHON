class user:
    def __init__(self,name):
        print(" welcome buddy")
        self.name=name
    def fun(self):
        print("name :",self.name)
o=user("virat")
o.fun()

o1=user("dhoni")
o1.fun()
print(user.__dict__)
print(o.__dict__)
print(o1.__dict__)