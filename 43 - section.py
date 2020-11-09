# JSON Module

import json

d = {
    "foo": "bar",
    "alice": 1,
    "wonderland": [1,2,3]
}

# Store
with open('mytext.json', 'w') as f:
    json.dump(d, f)


# Retrieve
with open("mytext.json", 'r') as f:
    d = json.load(f)
    print(d)


data = {
    "cats": [
        {"name": "Tubbs", "color": "white"},
        {"name": "pepper", "color": "black"}
    ]
}

# Formatting
json_str = json.dumps(data, indent = 2)
print(json.loads(json_str))