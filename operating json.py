import json
with open('s.json') as f:
    data=json.load(f)
print(f"temperature:{data['temp']}c")
print(f"humidity:{data['humidity']}")
print(f"weather :{data['description']}")
