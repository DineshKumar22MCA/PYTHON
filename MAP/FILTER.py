items = [(3456,"shoe",780),(3566,"phone",25300),(2587,"book",450),(5412,"pen",75)]
less_than_500 = lambda item:item[2]<500
filtered = list(filter(less_than_500,items))
print(filtered)
filtered = list(filter(lambda item:item[1][0]=='p',items))
print(filtered)