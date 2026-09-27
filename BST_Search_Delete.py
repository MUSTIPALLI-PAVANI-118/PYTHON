# Roll Number: CH.AI.U4AID25028

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def search(root, key):
    if root is None or root.data == key:
        return root

    if key < root.data:
        return search(root.left, key)

    return search(root.right, key)


def find_min(root):
    current = root

    while current.left is not None:
        current = current.left

    return current


def delete(root, key):
    if root is None:
        return root

    if key < root.data:
        root.left = delete(root.left, key)

    elif key > root.data:
        root.right = delete(root.right, key)

    else:
        # Node with no child
        if root.left is None and root.right is None:
            return None

        # Node with only right child
        if root.left is None:
            return root.right

        # Node with only left child
        if root.right is None:
            return root.left

        # Node with two children
        successor = find_min(root.right)
        root.data = successor.data
        root.right = delete(root.right, successor.data)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Get input from user
n = int(input("Enter the number of nodes: "))

values = list(map(int, input("Enter the values: ").split()))

# Create the Binary Search Tree
root = None

for value in values:
    root = insert(root, value)

# Get key from user
key = int(input("Enter the key to search and delete: "))

# Search and delete
if search(root, key):
    print("Element found")
    root = delete(root, key)
else:
    print("Element not found")

# Display inorder traversal after deletion
print("Inorder after deletion:", end=" ")
inorder(root)