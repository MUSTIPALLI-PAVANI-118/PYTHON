What are Control Statements?

Control statements are used to control the flow of execution of a program.
They decide which statement is executed and how many times it is executed.

2️⃣ Types of Control Statements in Python

Python control statements are mainly divided into:

Decision Making Statements

Looping Statements

Jump (Control Transfer) Statements

🔹 3️⃣ Decision Making Statements

Decision making statements execute code based on conditions.

3.1️⃣ if Statement
Purpose

Executes a block of code only if the condition is True.

Syntax
if condition:
    statement

Example
x = 10
if x > 0:
    print("Positive number")

3.2️⃣ if–else Statement
Purpose

Executes one block if condition is True, otherwise executes another block.

Syntax
if condition:
    statement1
else:
    statement2

Example
num = 5
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

3.3️⃣ if–elif–else Ladder
Purpose

Used to check multiple conditions.

Syntax
if condition1:
    statement1
elif condition2:
    statement2
else:
    statement3

Example
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Fail")

3.4️⃣ Nested if
Purpose

An if statement inside another if.

Example
x = 10
if x > 0:
    if x % 2 == 0:
        print("Positive Even Number")
