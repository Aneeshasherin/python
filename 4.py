str=input("Enter a strting: ")
a=input("Enter the word you want to check: ")
str1=str.split()
count=0
for i in str1:
    if i==a:
        count=count+1
print(count)      