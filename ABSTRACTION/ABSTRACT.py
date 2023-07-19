from abc import ABC,abstractmethod
class car(ABC):
    def mileage(self,speed):
        pass

class swift(car):
    def mileage(self,speed):
        print("24 km")

class audi(car):
    def mileage(self,speed):
        print("10 km")

class BMW(car):
    def mileage(self,speed):
        print("8 km")

s=swift()
s.mileage(24)

