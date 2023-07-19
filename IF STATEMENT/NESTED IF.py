
num = int(input("enter the number : "))
if num > 99 and num < 1000 and num%2 == 0:
    print(str(num) + " is a three digit even number")
elif num >99 and num < 1000 and num%2==1:
    print(num,"is a three digit odd number")

else:
    print(str(num) + " is a not three digit even number")


name = "Satya"
if name[0] == 'S' or name[0] == 's':
    print("the name starts with s")


age = 18
id = False

if age >= 18:
    if id :
        print("you can vote")
    else :
        print("apply for id")
else:
    print("you can't vote")

