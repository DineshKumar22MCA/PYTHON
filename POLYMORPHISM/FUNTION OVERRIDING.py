class office:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)

class office1(office):
    def __init__(self,name,age,roll):
        super().__init__(name, age)
        self.roll=roll

    def display(self):
        print(self.roll)
        print(self.name)
        print(self.age)

o=office1("virat",35,"batsman")
o.display()





