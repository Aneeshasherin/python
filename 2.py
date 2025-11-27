start=int(input("enter starting year:"))
end=int(input("enter year ending:"))
print(f"leap year from {start} to {end} are:")
for year in range(start,end+1):
    if(year % 4==0 and year % 100!=0) or (year % 400==0):
        print(year)