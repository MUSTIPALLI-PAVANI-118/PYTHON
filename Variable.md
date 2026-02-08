What is a Variable?

A variable is a name given to a memory location that stores a value.
In Python, a variable is created automatically when a value is assigned.

x = 10
name = "Python"

2️⃣ Why Variables are Used?

Variables are used to:

Store data

Reuse values

Make programs readable

Perform operations on data

Example:

a = 10
b = 20
sum = a + b
print(sum)

3️⃣ Variable Declaration in Python

Python does not require explicit declaration

Variable is created at runtime

x = 5

4️⃣ Dynamic Typing

Python is a dynamically typed language.
The type of a variable can change during execution.

x = 10      # int
x = "Hi"    # str

5️⃣ Rules for Naming Variables

✅ Rules:

Must start with a letter or _

Can contain letters, numbers, _

Cannot start with a number

Cannot use keywords

Case-sensitive

❌ Invalid:

1name = "A"
class = 10


✅ Valid:

name1 = "Pavani"
_total = 100

6️⃣ Variable Assignment Types
🔹 Single Assignment
x = 10

🔹 Multiple Assignment
a, b, c = 1, 2, 3

🔹 Same Value to Multiple Variables
x = y = z = 5

7️⃣ Checking Variable Type

Use type() function:

x = 10
print(type(x))

8️⃣ Checking Memory Address

Each variable refers to a memory location.

x = 10
print(id(x))

9️⃣ Variable Reassignment

Variable value can be changed.

x = 10
x = 20

🔟 Deleting a Variable

Use del keyword to delete a variable.

x = 10
del x

1️⃣1️⃣ Case Sensitivity

Python variables are case-sensitive.

a = 10
A = 20


Both are different variables.

1️⃣2️⃣ Constants in Python

Python does not have true constants.
By convention, uppercase names are used.

PI = 3.14

1️⃣3️⃣ Common Errors with Variables

❌ Using variable before assignment:

print(x)


❌ Invalid name:

2num = 10
