year=int(input("ENTER THE YEAR:"))
#CHECKING FOR LEAP YEAR
if year%400==0:
    print("ENTERED YEAR IS LEAP YEAR")
elif year%100==0:
    print("ENTERED YEAR IS NOT A LEAP YEAR")
elif year%4==0:
    print("ENTERED YEAR IS LEAP YEAR")
else:
    print("ENTERED YEAR IS NOT A LEAP YEAR")
