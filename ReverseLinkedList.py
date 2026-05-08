class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print("Original List:")
print_list(head)

head = reverse_list(head)

print("Reversed List:")
print_list(head)
