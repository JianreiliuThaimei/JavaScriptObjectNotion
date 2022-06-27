# import json


# class Laptop:
# 	name = 'My Laptop'
# 	processor = 'Intel Core'
# laptop1 = Laptop()
# laptop1.name = 'Dell Alienware'
# laptop1.processor = 'Intel Core i7'
# jsonStr = json.dumps(laptop1.__dict__)
# print(jsonStr)

import json
x = {
    "name": "David", 
    "class": "I", 
    "age": 6
    }
y=json.dumps(x)
print(y)
print(type(y))