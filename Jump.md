Jump / Control Transfer Statements

Jump statements change the normal flow of execution.

5.1️⃣ break Statement
Purpose

Terminates the loop immediately.

Example
for i in range(5):
    if i == 3:
        break
    print(i)

5.2️⃣ continue Statement
Purpose

Skips the current iteration and moves to the next.

Example
for i in range(5):
    if i == 2:
        continue
    print(i)

5.3️⃣ pass Statement
Purpose

Used as a placeholder where a statement is required.

Example
if True:
    pass

🔹 6️⃣ Indentation in Control Statements

Python uses indentation instead of braces { }.

✔ Correct:

if x > 0:
    print("Positive")


❌ Incorrect:

if x > 0:
print("Positive")

🔹 7️⃣ Common Errors

Missing indentation

Infinite loops

Wrong condition logic

Example of infinite loop:

while True:
    print("Hello")
