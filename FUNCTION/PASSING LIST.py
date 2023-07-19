def fun(list):
    for i in range(0,len(list)):
        list[i]=list[i].title()
        print(list[i])
name=["virat","dhoni","raina","'abd'"]
fun(name[:])
print(name)