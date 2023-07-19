name = 'hari'
like1 = 'apples'
like2 = 'bananas'

print(name + ' likes ' + like1 + ' and ' + like2)


text = '{} likes {} and {}'
print(text.format(name,like1,like2))

name1='dini'
frnd1='vicky'
love='samantha'

print(text.format(name1,frnd1,love))


print('{} likes {} and {}'.format(name,like1,like2))



text = '{0} likes {2} and {1}'
print(text.format(name,like1,like2))


text = '{name} likes {fruit1} and {fruit2}'
print(text.format(name='hari',fruit1='apples',fruit2='bananas'))
print(text.format(name='ravi',fruit2='grapes',fruit1='oranges'))
