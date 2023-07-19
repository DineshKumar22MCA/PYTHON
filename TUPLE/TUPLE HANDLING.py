tup = (2,3,4)
print(tup)
print(type(tup))
print()

# tup[1] = 5   - cannot be done - error
tup = (3,5,6)
print(tup)
print()

print(tup[1])
print(tup.index(6))
print()

tup = (3-1,4,5,4,4)
print(tup)
print(tup.count(4))
print()

for i in tup:
    print(i)
print()

if 3 in tup:
    print('yes')

if 3 not in tup:
    print('no')

if tup:
    print('tup is not empty')