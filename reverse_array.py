def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


arr = [10, 20, 30, 40, 50]

print("Original Array:", arr.copy())
print("Reversed Array:", reverse_array(arr))
