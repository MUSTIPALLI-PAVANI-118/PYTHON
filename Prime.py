n = int(input("ENTER THE VALUE OF n:"))
if n > 1:
    for i in range(2,n):
        if n%1==0:
            print(n,"is not a prime")
            break
    else:
        print(n,"is  a prime")
else:
    print(n,"is not a prime")
