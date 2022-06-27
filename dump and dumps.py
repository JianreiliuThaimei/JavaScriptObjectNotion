# dump
# import json
  
# # Data to be written
# dictionary ={
#     "name" : "sathiyajith",
#     "rollno" : 56,
#     "cgpa" : 8.6,
#     "phonenumber" : "9976770500"
# }
  
# with open("dump.json", "w") as outfile:
#     json.dump(dictionary, outfile)

# dumps
import json
    
# # Data to be written
dictionary ={
  "id": "04",
  "name": "sunil",
  "department": "HR"
}
    
# # Serializing json 
json_object = json.dumps(dictionary, indent = 4)
print(json_object)
print(type(json_object))