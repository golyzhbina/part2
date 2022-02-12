import json
from random import choice

with open("static/json/data.json", "rt", encoding="utf8") as f:
    data = json.loads(f.read())
keys = list(data.keys())
print(choice(keys))
