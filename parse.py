import json, os

files = []
base_path = 'raw_data'
for i in os.listdir(base_path):
    if i.endswith('.json'):
        full_path = '%s/%s' % (base_path, i)
        with open(full_path) as f:
            data = json.load(f)
            print(data)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
# print(data)
# print(data[0][0])
