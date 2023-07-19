class student:
    name="dinesh"
    age=25
    def  fun():
        print(student.name,)
        print(student.age)
student.fun()
print(student.__dict__)

print(getattr(student,"fun"))
getattr(student,"fun")()
print(student.__dict__)
student.__dict__["fun"]()