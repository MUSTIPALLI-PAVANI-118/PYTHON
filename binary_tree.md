# Binary Trees in Python

---

## Block 1 — Node class

```python
# A Node is one single box in the tree
# It holds a value, and knows its left and right child

class Node:

    def __init__(self, data):

        self.data  = data   # the value stored inside this node (e.g. 50)
        self.left  = None   # pointer to the left child  → starts empty
        self.right = None   # pointer to the right child → starts empty
```

---

## Block 2 — BST:Insert and Search

```python
# A Binary Search Tree keeps this rule at every node:
#   left child  < current node
#   right child > current node

class BinarySearchTree:

    def __init__(self):
        self.root = None   # the tree starts completely empty


    # ── INSERT ────────────────────────────────────────────────────────────────

    def insert(self, data):
        # called by the user — starts the recursive process from the root
        self.root = self._insert(self.root, data)


    def _insert(self, node, data):

        if node is None:
            return Node(data)       # empty spot found → create a new node here

        if data < node.data:
            node.left  = self._insert(node.left,  data)   # go LEFT (smaller)

        elif data > node.data:
            node.right = self._insert(node.right, data)   # go RIGHT (larger)

        # if data == node.data → duplicate, do nothing

        return node   # return this node back up to its parent


    # ── SEARCH ────────────────────────────────────────────────────────────────

    def search(self, data):
        # called by the user — starts searching from the root
        return self._search(self.root, data)


    def _search(self, node, data):

        if node is None:
            return False            # fell off the tree → value does not exist

        if data == node.data:
            return True             # found the value!

        if data < node.data:
            return self._search(node.left,  data)   # look in LEFT subtree

        return self._search(node.right, data)        # look in RIGHT subtree
```

---

## Block 3 — All 4 Traversals

```python
from collections import deque   # deque is used as a queue for level order

class Traversals:


    # ── INORDER: Left → Root → Right ──────────────────────────────────────────
    # On a BST, inorder ALWAYS gives values in sorted (ascending) order

    def inorder(self, node, result=None):

        if result is None:
            result = []             # create the result list on first call

        if node is None:
            return result           # base case: nothing to visit here

        self.inorder(node.left, result)    # step 1: go all the way left first
        result.append(node.data)           # step 2: visit the current node
        self.inorder(node.right, result)   # step 3: go right

        return result


    # ── PREORDER: Root → Left → Right ─────────────────────────────────────────
    # Visits the current node BEFORE its children
    # Useful for: printing tree structure, copying a tree

    def preorder(self, node, result=None):

        if result is None:
            result = []

        if node is None:
            return result

        result.append(node.data)            # step 1: visit current node FIRST
        self.preorder(node.left,  result)   # step 2: go left
        self.preorder(node.right, result)   # step 3: go right

        return result


    # ── POSTORDER: Left → Right → Root ────────────────────────────────────────
    # Visits the current node AFTER its children
    # Useful for: deleting a tree (delete children before parent)

    def postorder(self, node, result=None):

        if result is None:
            result = []

        if node is None:
            return result

        self.postorder(node.left,  result)   # step 1: go left
        self.postorder(node.right, result)   # step 2: go right
        result.append(node.data)             # step 3: visit current node LAST

        return result


    # ── LEVEL ORDER (BFS): level by level, top to bottom ──────────────────────
    # Uses a Queue — visit every node on level 1, then level 2, then level 3...

    def level_order(self, root):

        if root is None:
            return []

        result = []              # will hold the final order of values
        queue  = deque([root])   # start the queue with just the root node

        while queue:

            node = queue.popleft()           # take the front node out
            result.append(node.data)         # visit it

            if node.left:                    # if it has a left child →
                queue.append(node.left)      #     add left child to back of queue

            if node.right:                   # if it has a right child →
                queue.append(node.right)     #     add right child to back of queue

        return result
```

---

## Block 4 — Height, node count, leaf count, min and max

```python
class TreeProperties:


    # ── HEIGHT ────────────────────────────────────────────────────────────────
    # Height = number of EDGES on the longest path from root down to any leaf
    # Empty tree  → -1
    # Single node → 0

    def height(self, node):

        if node is None:
            return -1                          # no node here → height is -1

        left_h  = self.height(node.left)       # get height of left subtree
        right_h = self.height(node.right)      # get height of right subtree

        return 1 + max(left_h, right_h)        # 1 (for current node) + taller side


    # ── COUNT ALL NODES ───────────────────────────────────────────────────────
    # Recursively count: current node (1) + all nodes in left + all in right

    def count_nodes(self, node):

        if node is None:
            return 0                            # no node here → count is 0

        left_count  = self.count_nodes(node.left)    # count left subtree
        right_count = self.count_nodes(node.right)   # count right subtree

        return 1 + left_count + right_count     # 1 for current + both sides


    # ── COUNT LEAF NODES ──────────────────────────────────────────────────────
    # A leaf = a node with NO left child AND NO right child

    def count_leaves(self, node):

        if node is None:
            return 0                            # no node → 0 leaves

        if node.left is None and node.right is None:
            return 1                            # this node IS a leaf → count it

        left_leaves  = self.count_leaves(node.left)    # count leaves on the left
        right_leaves = self.count_leaves(node.right)   # count leaves on the right

        return left_leaves + right_leaves       # total leaves from both sides


    # ── FIND MINIMUM VALUE ────────────────────────────────────────────────────
    # In a BST the smallest value is always the LEFTMOST node
    # Keep going left until there is no more left child

    def find_min(self, node):

        while node.left is not None:   # keep moving left
            node = node.left

        return node.data               # the leftmost node holds the minimum


    # ── FIND MAXIMUM VALUE ────────────────────────────────────────────────────
    # In a BST the largest value is always the RIGHTMOST node
    # Keep going right until there is no more right child

    def find_max(self, node):

        while node.right is not None:  # keep moving right
            node = node.right

        return node.data               # the rightmost node holds the maximum
```

---

## Main driver 

```python
# ── Run this file directly:  python binary_tree.py ────────────────────────

if __name__ == '__main__':

    # ── Build a BST by inserting values one by one ──────────────────────────
    #
    #           50          ← root
    #          /  \
    #        30    70
    #       /  \     \
    #      20  40     80
    #
    # Left child is always smaller, right child is always larger

    bst = BinarySearchTree()

    bst.insert(50)   # becomes the root
    bst.insert(30)   # 30 < 50  → goes LEFT  of 50
    bst.insert(70)   # 70 > 50  → goes RIGHT of 50
    bst.insert(20)   # 20 < 50, 20 < 30 → goes LEFT  of 30
    bst.insert(40)   # 40 < 50, 40 > 30 → goes RIGHT of 30
    bst.insert(80)   # 80 > 50, 80 > 70 → goes RIGHT of 70


    print("=" * 50)
    print("  BLOCK 2 — Search")
    print("=" * 50)

    print("Search for 40:", bst.search(40))   # True  → 40 exists in the tree
    print("Search for 99:", bst.search(99))   # False → 99 does not exist


    print()
    print("=" * 50)
    print("  BLOCK 3 — Traversals")
    print("=" * 50)

    t = Traversals()

    # Inorder on a BST always gives sorted output
    print("Inorder   (L→Root→R):", t.inorder(bst.root))
    # Expected: [20, 30, 40, 50, 70, 80]

    # Preorder visits root before children
    print("Preorder  (Root→L→R):", t.preorder(bst.root))
    # Expected: [50, 30, 20, 40, 70, 80]

    # Postorder visits root after children
    print("Postorder (L→R→Root):", t.postorder(bst.root))
    # Expected: [20, 40, 30, 80, 70, 50]

    # Level order goes level by level (BFS)
    print("Level order (BFS)   :", t.level_order(bst.root))
    # Expected: [50, 30, 70, 20, 40, 80]


    print()
    print("=" * 50)
    print("  BLOCK 4 — Tree Properties")
    print("=" * 50)

    tp = TreeProperties()

    # Height = edges on longest root-to-leaf path
    print("Height     :", tp.height(bst.root))
    # Expected: 2   (path: 50 → 30 → 20  has 2 edges)

    # Count every node in the tree
    print("Node count :", tp.count_nodes(bst.root))
    # Expected: 6   (50, 30, 70, 20, 40, 80)

    # Count only leaf nodes (nodes with no children)
    print("Leaf count :", tp.count_leaves(bst.root))
    # Expected: 3   (20, 40, 80 have no children)

    # Minimum = leftmost value in a BST
    print("Minimum    :", tp.find_min(bst.root))
    # Expected: 20

    # Maximum = rightmost value in a BST
    print("Maximum    :", tp.find_max(bst.root))
    # Expected: 80

    print()
    print("All done!")
```

---

