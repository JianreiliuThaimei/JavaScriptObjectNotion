import json
list={"shopping_list":{ "choco":"15","Jelly":"50","Chuppa chupps":
    "30","UKmilk":"20",}}
item=input("enter the item:")
quantity=int(input("how much you want to buy:"))
a=list["shopping_list"][item]
r=int(a)-quantity
list["shopping_list"][item]=r
print(list)