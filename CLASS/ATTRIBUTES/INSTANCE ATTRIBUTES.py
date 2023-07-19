class user():
    name="dinesh"

o=user()

print(user.__dict__)
print(o.__dict__)
print(o.name)
print(o.__dict__)
o.name="vicky"
print(o.__dict__)
print(user.__dict__)
print(o.name)
print(user.name)
print(user.__dict__)
o2=user()
print(o2.name)

