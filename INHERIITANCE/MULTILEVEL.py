class grandfather:
    a=10
    def land(self):

        print(" grand father having a land")
class father(grandfather):
    def house(self):
        print(super().a)
        print("dad build a house")
class son(father):
    def car(self):
        print("son bought a car")

o=son()
o.land()
o.house()
o.car()