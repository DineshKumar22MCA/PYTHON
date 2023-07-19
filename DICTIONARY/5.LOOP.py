

player = {
    "name " : "virat",
    "score ": 100,
    "team " : "india",
    "jersey ": 18,
    "strike rate ": 200
}

for key,val in player.items():
    print("key : ",key)
    print("val : ",val)

for key in player.keys():
    print(key)

for key in sorted(player.keys()):
    print(player[key])
