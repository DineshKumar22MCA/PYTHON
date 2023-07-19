class student:
    name="virat"
    age=34
    def fun(self,gender):
        print(student.name)
        print(student.age)
        print(gender)

o=student()

'''o.fun()
student.fun(o)'''

o.fun("male")
print(o.fun("male"))
