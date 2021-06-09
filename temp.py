fruit={}
fruits=["Apple","Banana","Grapes","Apple","Apple","Banana","apple"]
for index in fruits:
 if index in fruit:
    fruit[index]+=1
 else:
    fruit[index]=1
print(fruit)
print("Len of fruit",len(fruit))

