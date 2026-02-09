Tuples in Python
1️⃣ What is a Tuple?

A tuple is a collection of elements stored in a single variable.
Tuples are ordered, immutable, and allow duplicate values.

t = (10, 20, 30)

2️⃣ Why Tuples are Used?

Tuples are used when:

Data should not be modified

Data needs to be protected from change

Faster access compared to lists

Fixed data like coordinates, days, months

Example:

days = ("Mon", "Tue", "Wed")

3️⃣ Creating Tuples
Normal Tuple
t1 = (1, 2, 3)

Tuple with Different Data Types
t2 = (10, "Python", 3.14)

Single Element Tuple (Important)
t3 = (5,)   # comma is mandatory

Empty Tuple
t4 = ()

4️⃣ Accessing Tuple Elements (Indexing)
t = (10, 20, 30)
print(t[0])   # 10
print(t[-1])  # 30

5️⃣ Tuple Slicing
t = (10, 20, 30, 40)
print(t[1:3])   # (20, 30)
print(t[:2])    # (10, 20)

6️⃣ Tuples are Immutable

👉 Once created, tuple elements cannot be changed.

❌ Invalid:

t = (10, 20)
t[0] = 5


✔ Valid:

t = (5, 20)

7️⃣ Tuple Operations
Concatenation (+)
a = (1, 2)
b = (3, 4)
print(a + b)

Repetition (*)
print((1, 2) * 3)

8️⃣ Tuple Methods

Tuples have very few methods.

Method	Use
count()	Count occurrences
index()	Find position

Example:

t = (1, 2, 2, 3)
print(t.count(2))
print(t.index(3))

9️⃣ Tuple Packing and Unpacking
Packing
t = 10, 20, 30

Unpacking
a, b, c = t
print(a, b, c)

🔟 Looping Through a Tuple
t = (10, 20, 30)
for i in t:
    print(i)

1️⃣1️⃣ Tuple vs List
Feature	Tuple	List
Mutable	❌	✅
Speed	Faster	Slower
Brackets	( )	[ ]
Methods	Few	Many
1️⃣2️⃣ Common Errors

❌ Missing comma in single element tuple:

t = (5)   # Not a tuple


✔ Correct:

t = (5,)
