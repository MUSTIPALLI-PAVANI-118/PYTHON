1. Variables in Python
What is a Variable?

A variable is a name given to a memory location that stores a value.
In Python, variables are created automatically when a value is assigned.

x = 10
name = "Python"

🔹 2. Characteristics of Variables in Python

No need to declare data type

Type is decided at runtime

Variable value can be changed

Case-sensitive

a = 10
a = "Hello"   # Valid

🔹 3. Rules for Naming Variables

✅ Valid rules:

Must start with a letter (a–z, A–Z) or underscore _

Can contain letters, digits, and _

Cannot start with a digit

Cannot be a keyword

❌ Invalid:

2name = "Python"   # Invalid
class = 10         # Keyword


✅ Valid:

name2 = "Pavani"
_total = 100

🔹 4. Variable Assignment Types
Single Assignment
x = 10

Multiple Assignment
a, b, c = 1, 2, 3

Same Value to Multiple Variables
x = y = z = 5

🔹 5. Dynamic Typing

Python is dynamically typed, meaning the variable type can change.

x = 10
x = "Python"

🔹 6. Checking Variable Type

Use type() function:

x = 10
print(type(x))   # <class 'int'>

📦 Data Types in Python
🔹 7. What is a Data Type?

A data type defines:

Type of value stored

Memory allocation

Operations allowed

🔹 8. Built-in Data Types
1️⃣ Integer (int)

Used to store whole numbers.

a = 10
b = -25

2️⃣ Floating Point (float)

Used to store decimal values.

x = 10.5
y = -3.14

3️⃣ String (str)

Used to store text data enclosed in quotes.

name = "Python"
msg = 'Hello World'

4️⃣ Boolean (bool)

Used to store True or False.

is_valid = True
is_empty = False

🔹 9. Complex Data Type (complex)

Used to store complex numbers.

c = 3 + 5j

🔹 10. Collection Data Types
📘 List (list)

Ordered

Mutable

Allows duplicate values

marks = [10, 20, 30]

📗 Tuple (tuple)

Ordered

Immutable

t = (1, 2, 3)

📙 Set (set)

Unordered

No duplicate values

s = {1, 2, 3}

📕 Dictionary (dict)

Stores data in key-value pairs

student = {
    "name": "Pavani",
    "age": 20
}

🔹 11. Type Conversion (Type Casting)
Implicit Conversion
x = 10
y = 2.5
z = x + y   # Result is float

Explicit Conversion
x = int("10")
y = float(5)
z = str(100)

🔹 12. Checking Memory Address
x = 10
print(id(x))

🔹 13. Mutable vs Immutable
Type	Mutable
int	❌
float	❌
str	❌
list	✅
dict	✅
set	✅
tuple	❌
🔹 14. Deleting Variables
x = 10
del x

🔹 15. Common Mistakes

❌ Adding string and integer:

"10" + 5


✅ Correct:

int("10") + 5
