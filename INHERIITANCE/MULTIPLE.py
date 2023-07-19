class father:
    def fishing(self):
        print("fishing in the sea")
    def chess(self):
        print("playing chess like dad")
    def former(self):
        print("dad doing agriculture")

class mother:
    def cooking(self):
        print("cooks very well")
    def chess(self):
        print("playing chess like a"
              " mother")
class son(father,mother):
    def ride(self):
        print(" bike riding")
o=son()
o.ride()
o.chess()
o.cooking()
o.former()
