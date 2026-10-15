def find_common_elements(arr1, arr2):
    common = []
    seen = set(arr2)

    for num in arr1:
        if num in seen:
            common.append(num)
            seen.remove(num)

    return common


arr1 = [10, 20, 30, 40, 50]
arr2 = [20, 40, 60, 80]

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Common Elements:", find_common_elements(arr1, arr2))
