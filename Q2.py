# Q2. Write a program to accept three integers and print the largest of the three.

x = float(input("Enter a first number : "))
y = float(input("Enter a second number : "))
z = float(input("Enter a third number : "))

if (x >= y) and (x >= z):
   largest = x
elif (y >= x) and (y >= z):
   largest = y
else:
   largest = z
print("The largest number is", largest)

'''Wrong Code 

if(x>y):
    print(x, "is the largest number")
elif(y>z):
    print(y, "is the largest number")
else:
    print(z, "is the largest number")'''