1️⃣ What is a Function?

A function is a block of reusable code that performs a specific task.
Instead of writing the same code again and again, we place it inside a function and call it whenever needed.

2️⃣ Why We Use Functions?

We use functions to:

Avoid code repetition

Improve code readability

Make programs modular

Simplify debugging

Reuse logic multiple times

Save development time

3️⃣ When We Use Functions?

We use functions when:

A task needs to be performed multiple times

A program becomes large and complex

We want to divide a program into smaller parts

The same logic is required in different places

We want easier testing and maintenance

4️⃣ Syntax of a Function
def function_name(parameters):
    statement(s)
    return value

5️⃣ Example: Function Without Parameters
When to use

When the task is fixed and does not depend on input.

def greet():
    print("Hello, Welcome to Python")

greet()

6️⃣ Example: Function With Parameters
When to use

When the function needs input values to work.

def add(a, b):
    return a + b

result = add(10, 20)
print(result)

7️⃣ Example: Function With Return Value
Why return is used

To send result back to the caller

To reuse the output

def square(n):
    return n * n

print(square(5))

8️⃣ Example: Function Without Return Value
def display(name):
    print("Hello", name)

display("Pavani")

9️⃣ Real-Life Example of Function Usage
Problem (Without Function)
a = 5
b = 6
print(a + b)

c = 10
d = 20
print(c + d)

Solution (With Function)
def add(x, y):
    return x + y

print(add(5, 6))
print(add(10, 20))


✔ Less code
✔ More readable
✔ Reusable

🔟 Built-in vs User-Defined Functions
Built-in Functions

Already provided by Python.

Examples:

print()
len()
type()
input()

User-Defined Functions

Created by the programmer.

def multiply(a, b):
    return a * b

1️⃣1️⃣ Advantages of Functions

Reusability

Reduced program length

Easy debugging

Better structure

Improves teamwork
