Exception Handling in Python
1️⃣ What is an Exception?

An exception is a runtime error that occurs while the program is executing and interrupts normal flow of the program.

Example:

x = 10 / 0   # ZeroDivisionError

2️⃣ Difference Between Error and Exception
Error	Exception
Syntax or logical mistake	Runtime problem
Stops program	Can be handled
Example: syntax error	Example: division by zero
3️⃣ Why Exception Handling is Used?

Exception handling is used to:

Prevent program crash

Handle runtime errors gracefully

Display user-friendly messages

Maintain normal program flow

4️⃣ Types of Common Exceptions
Exception	Cause
ZeroDivisionError	Divide by zero
ValueError	Invalid value
TypeError	Wrong data type
IndexError	Index out of range
KeyError	Invalid dictionary key
FileNotFoundError	File not found
5️⃣ try and except Block
Syntax
try:
    risky code
except ExceptionType:
    handling code

Example
try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")

6️⃣ Multiple except Blocks
try:
    x = int(input())
    y = int(input())
    print(x / y)
except ZeroDivisionError:
    print("Division by zero error")
except ValueError:
    print("Invalid input")

7️⃣ else Block

Executes when no exception occurs.

try:
    print(10 / 2)
except ZeroDivisionError:
    print("Error")
else:
    print("No error occurred")

8️⃣ finally Block

Executes always, whether exception occurs or not.

try:
    print(10 / 0)
except:
    print("Error")
finally:
    print("Program ended")

9️⃣ Handling File Exceptions
try:
    f = open("data.txt", "r")
except FileNotFoundError:
    print("File not found")

🔟 User-Defined Exceptions

Create your own exception using raise.

age = int(input())
if age < 18:
    raise Exception("Age must be 18 or above")

1️⃣1️⃣ Common Mistakes

❌ Catching all exceptions blindly:

except:
    pass


❌ Writing risky code outside try block
