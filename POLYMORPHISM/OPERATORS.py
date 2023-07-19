class user:
    def __init__(self,a,b):
        self.a=a
        self.b=b


    def __add__(self):
        print(self.a+self.b)


    def __sub__(self, a,b):
        print(a-b)

    def __truediv__(self,a,b):
        print(a/b)

o=user(10,12)
o.__add__()


