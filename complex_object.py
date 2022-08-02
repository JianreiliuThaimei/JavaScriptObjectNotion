# import json
# def is_complex_num(objct):
#     if '__complex__' in objct:
#         return complex(objct['real'], objct['img'])
#     return objct

# complex_object =json.loads('{"__complex__": true, "real": 4, "img": 5}', object_hook = is_complex_num)
# simple_object =json.loads('{"real": 4, "img": 3}', object_hook = is_complex_num)
# print("Complex_object: ",complex_object)
# print("Without complex object: ",simple_object)
# print(type(complex_object))
# print(type(simple_object))

# import json
# def encode_complex(object):
#     if inistance(object,complex):
#         return[object.real,object.img]
#     raise TypeError(repr(object)+"is not JSON serialized")
# complex_obj = json.dumps(2 + 3j,default=encode_complex)
# print(complex_obj)