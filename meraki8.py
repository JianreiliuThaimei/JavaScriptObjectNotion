import json
a=["neelam","programer","24","24000"]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]
e=["name","designation","age","salary"]
dic={}
dic1={}
dic2={}
dic3={}
dic4={}
i=0
while i<len(a):
  dic1[e[i]]=a[i]
  dic2[e[i]]=b[i]
  dic3[e[i]]=c[i]
  dic4[e[i]]=d[i]
  i=i+1
dic["emp1"]=dic1
dic["emp2"]=dic2
dic["emp3"]=dic3
dic["emp4"]=dic4
# print(dic)
with open("meraki8.json","w") as f:
  y=json.dump(dic,f,indent=4)
f.close()