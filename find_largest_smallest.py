def find_largest_smallest(arr):
    if not arr:
        return None

    largest = smallest = arr[0]

    for num in arr:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest


arr = [12, 45, 7, 89, 23, 4]

result = find_largest_smallest(arr)

if result:
    print("Largest:", result[0])
    print("Smallest:", result[1])
else:
    print("Array is empty")
