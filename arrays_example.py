# arrays_example.py

# Creating an array (list)
arr = [10, 20, 30, 40, 50]

# Accessing elements
print("First element:", arr[0])

# Adding elements
arr.append(60)
print("After append:", arr)

# Inserting at position
arr.insert(2, 25)
print("After insert:", arr)

# Removing element
arr.remove(30)
print("After remove:", arr)

# Looping through array
print("Array elements:")
for element in arr:
    print(element)

# Length of array
print("Length:", len(arr))
