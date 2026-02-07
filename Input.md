Input & Output (Detailed)
🔹 Output in Python

Used to display data on the screen.

print("Hello World")


Multiple values:

print("Age:", 20)

🔹 Input in Python

Used to take input from the user.

name = input("Enter your name: ")
print("Hello", name)


⚠️ Important Note

input() always returns string

Convert to required type

🔹 Type Conversion
age = int(input("Enter age: "))
price = float(input("Enter price: "))

🔹 Formatted Output
name = "Python"
version = 3.12
print(f"Language: {name}, Version: {version}")

🔹 Common Errors
age = input("Enter age: ")
print(age + 5)   # ❌ Error (string + int)


Correct way:

age = int(input("Enter age: "))
print(age + 5)
