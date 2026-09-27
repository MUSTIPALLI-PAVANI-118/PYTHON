#ROLL NO.:CH.AI.U4AID25028
# Function to maintain the Max Heap property
def heapify(array, heap_size, root):
    # Assume the root is the largest element
    largest = root

    # Calculate the left and right child indices
    left = 2 * root + 1
    right = 2 * root + 2

    # Check whether the left child is greater than the root
    if left < heap_size and array[left] > array[largest]:
        largest = left

    # Check whether the right child is greater
    if right < heap_size and array[right] > array[largest]:
        largest = right

    # If the root is not the largest, perform swapping
    if largest != root:
        array[root], array[largest] = array[largest], array[root]

        # Apply heapify to the affected subtree
        heapify(array, heap_size, largest)


# Function to perform Heap Sort
def heap_sort(array):
    n = len(array)

    # Build a Max Heap
    for index in range(n // 2 - 1, -1, -1):
        heapify(array, n, index)

    # Move the maximum element to the end
    for end in range(n - 1, 0, -1):
        # Swap the root with the last unsorted element
        array[0], array[end] = array[end], array[0]

        # Restore the Max Heap property
        heapify(array, end, 0)


# Read the number of elements
n = int(input("Enter the number of elements: "))

# Read the elements
values = list(map(int, input("Enter the elements: ").split()))

# Check whether exactly N elements were entered
if len(values) != n:
    print("Please enter exactly", n, "elements.")

else:
    # Perform Heap Sort
    heap_sort(values)

    # Display the sorted array
    print("Sorted array:", *values)