class student:
    name="dinesh"
    age =25
#get atributes
print(getattr(student,"name"))
print(getattr(student,"age"))
print(getattr(student,"gender","male"))
print("----------------------------------")
#dot notation
print(student.name)
print(student.age)

print("__________________________")

#set attributes

setattr(student,"name","vicky")
print(student.name)
setattr(student,"gender","male")
print(student.gender)
setattr(student,"city","chennai")
print(student.city)

print(student.__dict__)

delattr(student,"city")
print(student.__dict__)

del (student.gender)

print(student.__dict__)

