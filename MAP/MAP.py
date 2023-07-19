items = [(3456,"shoe",780),(3566,"phone",25300),(2587,"book",450),(5412,"pen",75)]
inr_usd = lambda item:(item[0],item[1],item[2]/74)
inr_usd2 = lambda item:(item[0],item[1],float("{:.2f}".format(item[2]/74)))
inr_usd3 = lambda item:(item[1],float("{:.2f}".format(item[2]/74)))
items_usd = list(map(inr_usd3,items))
print(items_usd)