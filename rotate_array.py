def rotate_array(arr, k):
    n = len(arr)

    if n == 0:
        return arr

    k = k % n

    return arr[-k:] + arr[:-k] if k else arr[:]


arr = [1, 2, 3, 4, 5]
k = 2

print("Original Array:", arr)
print("Rotated Array:", rotate_array(arr, k))
