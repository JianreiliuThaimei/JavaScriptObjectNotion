import json
dict={"id":1,"name":"value2","age":29}
file=open("meraki3.json","w")
json.dump(dict,file,indent=3)
file.close()