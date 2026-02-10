File Handling in Python
1️⃣ What is File Handling?

File handling is used to store data permanently in files and read data back whenever required.
Files help in saving data even after the program ends.

2️⃣ Why File Handling is Used?

File handling is used to:

Store data permanently

Read large amounts of data

Maintain records (student data, logs, reports)

Share data between programs

Example uses:

Student records

Log files

Configuration files

3️⃣ Types of Files
🔹 Text Files

Store data as text

Examples: .txt, .csv

🔹 Binary Files

Store data in binary format

Examples: .bin, .dat, .jpg

👉 In basics, we mostly use text files.

4️⃣ Opening a File
Syntax
file = open("filename", "mode")

Common File Modes
Mode	Meaning
r	Read
w	Write (overwrite)
a	Append
r+	Read + Write
w+	Write + Read
a+	Append + Read
5️⃣ Writing to a File
Example
f = open("data.txt", "w")
f.write("Hello Python")
f.close()


👉 If file does not exist, it will be created automatically.

6️⃣ Reading from a File
read()
f = open("data.txt", "r")
content = f.read()
print(content)
f.close()

readline()
f.readline()

readlines()
f.readlines()

7️⃣ Appending to a File
f = open("data.txt", "a")
f.write("\nNew line added")
f.close()


👉 Existing data is not deleted.

8️⃣ Closing a File
f.close()


👉 Always close files to:

Free memory

Avoid data loss

9️⃣ Using with Statement (Recommended)

Automatically closes the file.

with open("data.txt", "r") as f:
    print(f.read())


✔ Safe
✔ Clean
✔ Best practice

🔟 Checking File Existence
import os

if os.path.exists("data.txt"):
    print("File exists")

1️⃣1️⃣ File Handling Example Program
with open("student.txt", "w") as f:
    f.write("Name: Pavani\nAge: 20")


Reading:

with open("student.txt", "r") as f:
    print(f.read())

1️⃣2️⃣ Common Errors

❌ Reading non-existing file:

open("abc.txt", "r")


❌ Forgetting to close file

1️⃣3️⃣ Summary (Exam Ready)

File handling stores data permanently

open() is used to open files

Different modes control file operations

with statement is best practice

Always close files
