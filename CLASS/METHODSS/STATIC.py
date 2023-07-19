class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def fun(self):
        print(self.name,self.age)
    @staticmethod
    def welcome():
        print("welcome sunny")

o=user("mia",35)
o.fun()
o.welcome()

o1=user("dani dani",29)
o1.fun()
o1.welcome()