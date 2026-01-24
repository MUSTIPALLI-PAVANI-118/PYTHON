operator=input("ENTER OPERATOR(+,-,*,/)")
num1=int(input("enter num1 value:"))
num2=int(input("enter num2 value:"))
match operator:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)
    case _:
        print("invalid input")
