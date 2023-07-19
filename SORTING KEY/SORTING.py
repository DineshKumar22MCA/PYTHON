item=[(2,"c",250),(3,"a",150),(1,"b",132)]
item.sort()
print(item)
item.sort(key=lambda item:item[1])
print(item)
item.sort(key=lambda item:item[1],reverse=True)
print(item)
