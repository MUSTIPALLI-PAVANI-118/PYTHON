def remove_duplicates(arr):
    unique = []
    seen = set()

    for num in arr:
        if num not in seen:
            seen.add(num)
            unique.append(num)

    return unique


arr = [10, 20, 10, 30, 20, 40, 50, 40]

print("Original Array:", arr)
print("Without Duplicates:", remove_duplicates(arr))
