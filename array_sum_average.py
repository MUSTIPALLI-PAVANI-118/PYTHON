def sum_and_average(arr):
    if not arr:
        return 0, None

    total = sum(arr)
    average = total / len(arr)

    return total, average


arr = [10, 20, 30, 40, 50]

total, average = sum_and_average(arr)

print("Array:", arr)
print("Sum:", total)
print("Average:", average)
