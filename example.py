# convert json to python
# import json
# x='{"name":"john","age":30,"city":"NY"}'
# y=json.loads(x)
# print(y["age"])

# convert python to json
import json
x={"name":"john",
   "age":30,
   "city":"NY"
   }
y=json.dumps(x)
print(y)
print(type(y))

# import json
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))


