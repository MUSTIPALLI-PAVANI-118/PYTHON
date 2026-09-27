#ROLL N0.:CH.AI.U4AID25028
# Class representing a node of the AVL Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


# Function to obtain the height of a node
def get_height(node):
    if node is None:
        return 0

    return node.height


# Function to calculate the balance factor
def get_balance(node):
    if node is None:
        return 0

    return get_height(node.left) - get_height(node.right)


# Function to perform a right rotation
def right_rotate(y):
    # Store the left child
    x = y.left

    # Store the right subtree of the left child
    temporary_subtree = x.right

    # Perform the rotation
    x.right = y
    y.left = temporary_subtree

    # Update the heights
    y.height = 1 + max(
        get_height(y.left),
        get_height(y.right)
    )

    x.height = 1 + max(
        get_height(x.left),
        get_height(x.right)
    )

    # Return the new root
    return x


# Function to perform a left rotation
def left_rotate(x):
    # Store the right child
    y = x.right

    # Store the left subtree of the right child
    temporary_subtree = y.left

    # Perform the rotation
    y.left = x
    x.right = temporary_subtree

    # Update the heights
    x.height = 1 + max(
        get_height(x.left),
        get_height(x.right)
    )

    y.height = 1 + max(
        get_height(y.left),
        get_height(y.right)
    )

    # Return the new root
    return y


# Function to insert a value into the AVL Tree
def insert(root, value):
    # Perform normal BST insertion
    if root is None:
        return Node(value)

    if value < root.data:
        root.left = insert(root.left, value)

    elif value > root.data:
        root.right = insert(root.right, value)

    else:
        # Duplicate values are not inserted
        return root

    # Update the height
    root.height = 1 + max(
        get_height(root.left),
        get_height(root.right)
    )

    # Calculate the balance factor
    balance = get_balance(root)

    # Left-Left case
    if balance > 1 and value < root.left.data:
        return right_rotate(root)

    # Right-Right case
    if balance < -1 and value > root.right.data:
        return left_rotate(root)

    # Left-Right case
    if balance > 1 and value > root.left.data:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Right-Left case
    if balance < -1 and value < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


# Function to find the smallest node
def find_minimum(node):
    current = node

    # Move to the leftmost node
    while current.left is not None:
        current = current.left

    return current


# Function to delete a node from the AVL Tree
def delete_node(root, value):
    # Return if the tree is empty
    if root is None:
        return root

    # Search for the node to be deleted
    if value < root.data:
        root.left = delete_node(root.left, value)

    elif value > root.data:
        root.right = delete_node(root.right, value)

    else:
        # Case 1 and Case 2:
        # Node has no child or only one child
        if root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        # Case 3:
        # Node has two children
        successor = find_minimum(root.right)

        # Copy the Inorder successor's value
        root.data = successor.data

        # Delete the Inorder successor
        root.right = delete_node(
            root.right,
            successor.data
        )

    # Return if the tree becomes empty
    if root is None:
        return root

    # Update the height
    root.height = 1 + max(
        get_height(root.left),
        get_height(root.right)
    )

    # Calculate the balance factor
    balance = get_balance(root)

    # Left-Left case
    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)

    # Left-Right case
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Right-Right case
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)

    # Right-Left case
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


# Function to perform Inorder traversal
def inorder(root, result):
    if root is not None:
        inorder(root.left, result)
        result.append(root.data)
        inorder(root.right, result)


# Read the number of nodes
n = int(input("Enter the number of nodes: "))

# Read the node values
values = list(
    map(int, input("Enter the node values: ").split())
)

# Check whether exactly N values were entered
if len(values) != n:
    print("Please enter exactly", n, "values.")

else:
    # Create an empty AVL Tree
    root = None

    # Insert every value into the AVL Tree
    for value in values:
        root = insert(root, value)

    # Read the node to be deleted
    delete_value = int(
        input("Enter the node to be deleted: ")
    )

    # Delete the specified node
    root = delete_node(root, delete_value)

    # Store the Inorder traversal
    inorder_result = []

    # Perform Inorder traversal
    inorder(root, inorder_result)

    # Display the updated tree
    print(
        "Inorder after deletion:",
        *inorder_result
    )