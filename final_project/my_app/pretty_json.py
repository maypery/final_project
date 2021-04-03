import json

with open('api_employees.json') as f:
    data = json.load(f)
with open('employees.json', 'w') as file:
    json.dump(data, file, indent=2)