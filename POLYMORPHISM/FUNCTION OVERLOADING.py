class over:
    def add(self):
        print("hello world")

class over2(over):
    def add(self,i,j):
        return i+j


o=over2()

print(o.add(10,10))
o1=over()
o1.add()
