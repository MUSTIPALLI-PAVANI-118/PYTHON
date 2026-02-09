Lists in Python
1️⃣ What is a List?

A list is a collection of elements stored in a single variable.
Lists can store multiple values of different data types.

👉 Lists are ordered, mutable, and allow duplicates.

marks = [10, 20, 30]

2️⃣ Why Lists are Used?

Lists are used to:

Store multiple values together

Avoid using many variables

Perform operations on grouped data

Handle dynamic data (size can change)

Example:

names = ["Pavani", "Anu", "Ravi"]

3️⃣ Creating a List
Simple List
numbers = [1, 2, 3, 4]

Mixed Data Types
data = [10, "Python", 3.5, True]

Empty List
empty = []

4️⃣ Accessing List Elements (Indexing)

Index starts from 0.

lst = [10, 20, 30]
print(lst[0])   # 10
print(lst[2])   # 30

Negative Indexing
print(lst[-1])  # 30

5️⃣ List Slicing

Used to extract part of a list.

lst = [10, 20, 30, 40, 50]
print(lst[1:4])   # [20, 30, 40]
print(lst[:3])    # [10, 20, 30]
print(lst[2:])    # [30, 40, 50]

6️⃣ Lists are Mutable

👉 List elements can be changed.

lst = [10, 20, 30]
lst[1] = 25
print(lst)

7️⃣ Adding Elements to a List
append() – adds one element at end
lst.append(40)

insert() – adds at specific position
lst.insert(1, 15)

extend() – adds multiple elements
lst.extend([50, 60])

8️⃣ Removing Elements from a List
remove() – removes specific value
lst.remove(20)

pop() – removes by index
lst.pop(1)

clear() – removes all elements
lst.clear()

9️⃣ Common List Methods
Method	Use
append()	Add element
insert()	Add at position
remove()	Remove value
pop()	Remove by index
sort()	Sort list
reverse()	Reverse list
count()	Count value
index()	Find index

Example:

lst = [3, 1, 2]
lst.sort()
print(lst)

🔟 Length of a List
lst = [10, 20, 30]
print(len(lst))

1️⃣1️⃣ Looping Through a List
Using for loop
lst = [10, 20, 30]
for i in lst:
    print(i)

1️⃣2️⃣ List Concatenation & Repetition
a = [1, 2]
b = [3, 4]
print(a + b)
print(a * 3)

1️⃣3️⃣ Nested Lists

List inside another list.

matrix = [[1, 2], [3, 4]]
print(matrix[0][1])  # 2

1️⃣4️⃣ List vs String
Feature	List	String
Mutable	✅	❌
Data type	Any	Characters
Brackets	[ ]	Quotes
1️⃣5️⃣ Common Errors in Lists

❌ Index error:

lst = [1, 2]
print(lst[5])


❌ Removing non-existing element:

lst.remove(100)
