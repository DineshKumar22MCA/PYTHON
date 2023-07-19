import functools
vals = [4,7,8,4,3]
sum = functools.reduce(lambda x,y:x+y,vals)
print(sum)


chars = ['pyt','h','o','n']
word = functools.reduce(lambda x,y:x+y,chars)
print(word)