# ROLL NO.:CH.AI.U4AID25028
# Find Maximum and Minimum in an Array

def find_max_min(arr, low, high):

    # Base case: only one element
    if low == high:
        return arr[low], arr[low]

    # Divide the array into two parts
    mid = (low + high) // 2

    # Find maximum and minimum in the left part
    left_max, left_min = find_max_min(arr, low, mid)

    # Find maximum and minimum in the right part
    right_max, right_min = find_max_min(arr, mid + 1, high)

    # Combine the results
    maximum = max(left_max, right_max)
    minimum = min(left_min, right_min)

    return maximum, minimum
# Read input
n = int(input("Enter the number of elements: "))

arr = list(map(int, input("Enter the array elements: ").split()))

# Find maximum and minimum
maximum, minimum = find_max_min(arr, 0, n - 1)

# Display the result
print("\nDivide and Conquer Result:")
print("Maximum element:", maximum)
print("Minimum element:", minimum)
print("Maximum and minimum found successfully.")
