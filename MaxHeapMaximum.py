#ROLL NO.:CH.AI.U4AID25028
# Function to insert an element into the Max Heap
def insert_max_heap(heap, value):
    # Add the new element at the end
    heap.append(value)

    # Get the index of the inserted element
    index = len(heap) - 1

    # Move the element upward if it is greater than its parent
    while index > 0:
        parent = (index - 1) // 2

        # Stop if the Max Heap property is satisfied
        if heap[parent] >= heap[index]:
            break

        # Swap the element with its parent
        heap[parent], heap[index] = heap[index], heap[parent]

        # Move to the parent's position
        index = parent


# Read the number of elements
n = int(input("Enter the number of elements: "))

# Read the elements
values = list(map(int, input("Enter the elements: ").split()))

# Check whether the correct number of elements was entered
if len(values) != n:
    print("Please enter exactly", n, "elements.")

else:
    # Create an empty Max Heap
    max_heap = []

    # Insert every value into the Max Heap
    for value in values:
        insert_max_heap(max_heap, value)

    # Display the Max Heap
    print("Max Heap:", *max_heap)

    # The root contains the maximum element
    print("Maximum element:", max_heap[0])