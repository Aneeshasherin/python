a=int(input("Enter a numbers: "))
b=int(input("Enter a numbers: "))
while(b!=0):
    r=a%b
    a=b
    b=r
print("GCD of given number is: ",a)

