import json
j= {'4': 5, '6': 7, '1': 3, '2': 4}
print("Original String:")
print(j)
print("\nJSON data:")
print(json.dumps(j, sort_keys=True, indent=4))
print(type(j))