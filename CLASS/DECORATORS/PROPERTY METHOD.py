class student:
    def __init__(self,total):
        self._total=total


    def average(self):
        return self._total/5

    def getter(self):
        return self._total

    def setter(self,t):
        if t<0 or t>500:
            print("invalid number")
        else:
            self._total=t

    total=property(getter,setter)

o=student(440)
print(o.total)
print(o.average())
o.total=550
print(o.total)
print(o.average())