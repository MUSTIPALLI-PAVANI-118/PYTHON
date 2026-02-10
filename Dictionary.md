Dictionaries in Python
1️⃣ What is a Dictionary?

A dictionary is a collection of data stored in key–value pairs.
Dictionaries are unordered, mutable, and keys must be unique.

student = {
    "name": "Pavani",
    "age": 20
}

2️⃣ Why Dictionaries are Used?

Dictionaries are used when:

Data has a meaningful relationship (key → value)

Fast data retrieval is needed

Data needs to be updated frequently

Working with real-world data like student records, user details

Example:

marks = {"Maths": 90, "Science": 85}

3️⃣ Creating Dictionaries
Normal Dictionary
d1 = {"a": 1, "b": 2}

Empty Dictionary
d2 = {}

Using dict() Constructor
d3 = dict(name="Python", version=3)

4️⃣ Accessing Dictionary Values

Access values using keys, not index.

student = {"name": "Pavani", "age": 20}
print(student["name"])


⚠️ Using wrong key causes KeyError.

Safe way:

print(student.get("age"))

5️⃣ Modifying Dictionary
Change Value
student["age"] = 21

Add New Key-Value Pair
student["course"] = "Python"

6️⃣ Removing Elements
pop()
student.pop("age")

del
del student["name"]

clear()
student.clear()

7️⃣ Dictionary Methods
Method	Use
keys()	Returns all keys
values()	Returns all values
items()	Returns key-value pairs
get()	Access value safely
pop()	Remove item
update()	Update dictionary

Example:

print(student.keys())
print(student.values())

8️⃣ Looping Through Dictionary
Loop Through Keys
for key in student:
    print(key)

Loop Through Values
for value in student.values():
    print(value)

Loop Through Key-Value
for k, v in student.items():
    print(k, v)

9️⃣ Nested Dictionary
students = {
    "s1": {"name": "A", "age": 20},
    "s2": {"name": "B", "age": 21}
}

🔟 Dictionary vs List
Feature	Dictionary	List
Storage	Key-Value	Values
Access	By key	By index
Duplicate keys	❌	Allowed
Mutable	✅	✅
1️⃣1️⃣ Common Errors

❌ Accessing using index:

student[0]


❌ Duplicate keys:

{"a": 1, "a": 2}   # Last value kept

1️⃣2️⃣ Summary (Exam Ready)

Dictionary stores key-value pairs

Keys must be unique

Values can be modified

Used for structured data

Very fast lookup
