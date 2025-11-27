x=int(input("enter a number: "))
y=int(input("enter a number: "))
z=int(input("enter a number: "))
if (x>y and x>z):
    print("the greatest number is",x)
elif (y>x and y>z):
    print("the greatest number is",y)
else:
    print("the greatest number is",z)
    