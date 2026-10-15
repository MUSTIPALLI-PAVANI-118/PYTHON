def move_zeros(arr):
    position = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[position], arr[i] = arr[i], arr[position]
            position += 1

    return arr


arr = [0, 1, 0, 3, 12, 0, 5]

print("Original Array:", arr.copy())
print("Updated Array:", move_zeros(arr))
