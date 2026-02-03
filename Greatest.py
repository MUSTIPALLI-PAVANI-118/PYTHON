#Find the greatest of four numbers
a=int(input("enter the a value:"))
b=int(input("enter the b value:"))
c=int(input("enter the c value:"))
d=int(input("enter the d value:"))
if a>=b and a>=c and a>=d:
  print(a," is the greatest number")
elif b>=a and b>=c and b>=d:
  print(b," is the greatest number")
elif c>=a and c>=b and c>=d:
  print(c," is the greatest number")
else:
  print(d," is the greatest number")
