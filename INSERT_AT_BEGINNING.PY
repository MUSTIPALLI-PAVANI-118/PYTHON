def insert_at_beginning(self, data):
    new_node = Node(data)

    if self.head is None:
        new_node.next = new_node
        self.head = new_node
        return

    temp = self.head
    while temp.next != self.head:
        temp = temp.next

    temp.next = new_node
    new_node.next = self.head
    self.head = new_node
