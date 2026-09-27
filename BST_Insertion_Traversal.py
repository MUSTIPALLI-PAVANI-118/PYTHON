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


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Get input from user
n = int(input("Enter the number of nodes: "))

values = list(map(int, input("Enter the values: ").split()))

# Create the Binary Search Tree
root = None

for value in values:
    root = insert(root, value)

# Display traversals
print("\nInorder traversal:", end=" ")
inorder(root)

print("\nPreorder traversal:", end=" ")
preorder(root)

print("\nPostorder traversal:", end=" ")
postorder(root)