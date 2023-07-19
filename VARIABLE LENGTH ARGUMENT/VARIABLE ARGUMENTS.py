

def total(*ab): #  *args -tuple
    sum=0
    for i in ab:
        sum=sum+i
    return(sum)

print(total(10,20,30,40,50))


