a = int(input("ENTER a VALUE:"))
b = int(input("ENTER b VALUE:"))

print("simple calculator")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
choice = int(input("enter your choice:"))
if choice == 1:
    print("ADDITION OF TWO NUMBERS IS " , a+b)
elif choice == 2:
    print("SUBTRACTION OF TWO NUMBERS IS " , a - b)
elif choice == 3:
    print("MULTIPLICATION OF NUMBERS IS " , a*b)
elif choice == 4:
    if b != 0:
        print("DIVISION OF TWO NUMBERS IS", a / b)
    else:
        print("Division by zero not allowed")

else:
    print("INVALID INPUT")
