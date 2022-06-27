import json
x = {
    "name": "Jian", 
     
    "age": 21,
    "city":"Mexico"
    }
y=json.dumps(x)
print("\nPython_object:")
print(y)
print(type(y))