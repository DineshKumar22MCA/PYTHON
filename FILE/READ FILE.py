f = open("textt.txt","r")
print(f.readline())
print(f.readable())
print(f.readlines())
print(f.close())

f=open("textt.txt","r")
for i in f:
    print(i)
    print(f.close())
