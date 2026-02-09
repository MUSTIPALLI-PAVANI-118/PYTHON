Strings in Python
1️⃣ What is a String?

A string is a sequence of characters used to store text data.
In Python, strings are written inside single quotes ' ', double quotes " ", or triple quotes ''' '''.

name = "Python"
course = 'Programming'

2️⃣ Why Strings are Used?

Strings are used to:

Store names, messages, sentences

Handle user input

Display output

Process text data

Examples:

username = "Pavani"
message = "Welcome to Python"

3️⃣ Creating Strings
Using Single Quotes
s1 = 'Hello'

Using Double Quotes
s2 = "Hello"

Using Triple Quotes (Multiline Strings)
s3 = """This is
a multi-line
string"""

4️⃣ Accessing Characters (Indexing)

Each character in a string has an index number starting from 0.

s = "Python"
print(s[0])   # P
print(s[3])   # h

Negative Indexing
print(s[-1])  # n
print(s[-2])  # o

5️⃣ String Slicing

Used to extract a part of a string.

Syntax
string[start : end]

Example
s = "Python"
print(s[0:4])   # Pyth
print(s[2:])    # thon
print(s[:3])    # Pyt

6️⃣ String is Immutable

👉 Strings cannot be changed once created.

❌ Invalid:

s = "Python"
s[0] = 'J'


✔ Correct:

s = "Python"
s = "Jython"

7️⃣ String Operations
Concatenation (+)
a = "Hello"
b = "World"
print(a + " " + b)

Repetition (*)
print("Hi " * 3)

8️⃣ Common String Methods
Method	Description
lower()	Converts to lowercase
upper()	Converts to uppercase
title()	Capitalizes first letter
strip()	Removes spaces
replace()	Replaces text
split()	Splits string
Example
s = " Python Programming "
print(s.strip())
print(s.upper())
print(s.replace("Python", "Java"))

9️⃣ Checking String Length
s = "Python"
print(len(s))

🔟 String Formatting
Using f-strings (Recommended)
name = "Pavani"
age = 20
print(f"My name is {name} and age is {age}")

1️⃣1️⃣ Escape Characters
Escape	Meaning
\n	New line
\t	Tab
\'	Single quote
\"	Double quote

Example:

print("Hello\nPython")

1️⃣2️⃣ String Membership Operators
s = "Python"
print("Py" in s)     # True
print("Java" not in s)  # True

1️⃣3️⃣ Looping Through a String
s = "Python"
for ch in s:
    print(ch)

1️⃣4️⃣ Common Errors in Strings

❌ Index out of range:

s = "Hi"
print(s[5])


❌ Trying to modify string:

s[0] = 'H'
