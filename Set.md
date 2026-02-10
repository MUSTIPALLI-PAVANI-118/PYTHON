Sets in Python
1️⃣ What is a Set?

A set is a collection of unique elements stored in a single variable.
Sets are unordered, mutable, and do not allow duplicate values.

s = {10, 20, 30}

2️⃣ Why Sets are Used?

Sets are used when:

Duplicate values must be removed

Order of elements does not matter

Fast membership checking is needed

Mathematical set operations are required

Example:

nums = {1, 2, 2, 3}
print(nums)   # {1, 2, 3}

3️⃣ Creating Sets
Normal Set
s1 = {1, 2, 3}

Set with Mixed Data Types
s2 = {10, "Python", 3.5}

Empty Set (Important)
s3 = set()     # {} creates dictionary

4️⃣ Accessing Set Elements

👉 Sets are unordered, so indexing is not supported.

❌ Invalid:

s = {1, 2, 3}
print(s[0])


✔ Correct:

for i in s:
    print(i)

5️⃣ Adding Elements to a Set
add() – add single element
s.add(40)

update() – add multiple elements
s.update([50, 60])

6️⃣ Removing Elements from a Set
remove() – removes element (error if not found)
s.remove(20)

discard() – removes element (no error)
s.discard(100)

pop() – removes random element
s.pop()

clear() – removes all elements
s.clear()

7️⃣ Set Operations
Union (|)
a = {1, 2}
b = {2, 3}
print(a | b)

Intersection (&)
print(a & b)

Difference (-)
print(a - b)

Symmetric Difference (^)
print(a ^ b)

8️⃣ Membership Testing
s = {10, 20, 30}
print(20 in s)
print(50 not in s)

9️⃣ Set Methods
Method	Use
add()	Add element
update()	Add many
remove()	Remove element
discard()	Safe remove
pop()	Remove random
clear()	Empty set
🔟 Frozen Set

A frozenset is an immutable set.

fs = frozenset([1, 2, 3])


👉 Elements cannot be added or removed.

1️⃣1️⃣ Set vs List vs Tuple
Feature	Set	List	Tuple
Order	❌	✅	✅
Duplicates	❌	✅	✅
Mutable	✅	✅	❌
1️⃣2️⃣ Common Errors

❌ Creating empty set wrongly:

s = {}   # dictionary


✔ Correct:

s = set()

1️⃣3️⃣ Summary (Exam Ready)

Set stores unique elements

No indexing or slicing

Useful for removing duplicates

Supports mathematical operations

Faster membership checking
