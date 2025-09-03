import json
players = [
    {'id' : 101, 'name' : 'jaiswal'},
    {'id' : 102, 'name' : 'gill'}
]

print(players)

with open('player.json', 'w') as file:
    json.dump(players, file)

with open('player.json', 'r') as reader:
    players_from_json = json.load(reader)
    print(players_from_json)