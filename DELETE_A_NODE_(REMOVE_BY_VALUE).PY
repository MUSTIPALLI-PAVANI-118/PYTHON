def delete(self, key):
    if self.head is None:
        return

    curr = self.head
    prev = None

    while True:
        if curr.data == key:
            if prev:
                prev.next = curr.next
            else:
                # deleting head
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = curr.next
                self.head = curr.next
            return

        prev = curr
        curr = curr.next

        if curr == self.head:
            print("Value not found")
            return
