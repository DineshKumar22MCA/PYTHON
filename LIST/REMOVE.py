

players = ['virat','dhoni','abd','raina']

print(players)
print()

#del
del players[3]
print(players)
print()

#pop()
players = ['virat','dhoni','abd','raina']
print(players)
x = players.pop(3)
print(x,"has been deleted")
print(players)
print()

#remove by value
players.remove('dhoni')
print(players)