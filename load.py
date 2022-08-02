# import json
# f = open('data.json')
# data = json.load(f)
# for i in data['emp_details']:
#     print(i)
#     print(type(data))
# f.close()

import json
with open("user.json","r") as f:
    x=json.load(f)
print(x)
print(type(x))