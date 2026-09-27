#ROLL NO.:CH.AI.U4AID25028
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

    # Update the height of the current node
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

    # Return the unchanged root
    return root


# Function to perform Inorder traversal
def inorder(root, result):
    if root is not None:
        inorder(root.left, result)
        result.append(root.data)
        inorder(root.right, result)


# Function to perform Preorder traversal
def preorder(root, result):
    if root is not None:
        result.append(root.data)
        preorder(root.left, result)
        preorder(root.right, result)


# Function to perform Postorder traversal
def postorder(root, result):
    if root is not None:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.data)


# Read the number of nodes
n = int(input("Enter the number of nodes: "))

# Read the node values
values = list(
    map(int, input("Enter the node values: ").split())
)

# Check the number of values
if len(values) != n:
    print("Please enter exactly", n, "values.")

else:
    # Initially, the AVL Tree is empty
    root = None

    # Insert every value into the AVL Tree
    for value in values:
        root = insert(root, value)

    # Lists for storing the traversal results
    inorder_result = []
    preorder_result = []
    postorder_result = []

    # Perform the three traversals
    inorder(root, inorder_result)
    preorder(root, preorder_result)
    postorder(root, postorder_result)

    # Display the traversal sequences
    print("Inorder:", *inorder_result)
    print("Preorder:", *preorder_result)
    print("Postorder:", *postorder_result)