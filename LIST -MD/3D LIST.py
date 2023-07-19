tn = ['chennai','ooty','selam']
kerala = ['idukki','alapey','wayanad']
ap = ['tada','nellur','tirupathy']
india = [tn,kerala,ap]
num = [1,2,3],[4,5,6],[7,8,9]
print(india)
print(india[0])
print(india[0][0])
print(india[0:2])
print(india[0][0:2])
print(num)
print()

tn.remove("selam")
print(india)
print()

tn.append("karur")
print(india)
print()

india[0][0] = "selam"
print(india)
print()

import copy
states = copy.deepcopy(india)
print(states)

for i in states:
    print(i)