#  Q21. What will the output of the following code fragment?
        fruit={}
        Fruits=["Apple","Banana","Grapes","Apple","Apple","Banana","apple"]
       for index in Fruits:
       if index in fruit:
       fruit[index]+=1
      else:
       fruit[index]=1
       print(fruit)
       rint("Len of fruit",len(fruit))