def second_largest(arr):
    largest = float("-inf")
    second = float("-inf")

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num

    if second == float("-inf"):
        return None

    return second


arr = [10, 25, 40, 15, 40, 30]

result = second_largest(arr)

if result is not None:
    print("Second Largest:", result)
else:
    print("Second largest element does not exist")
