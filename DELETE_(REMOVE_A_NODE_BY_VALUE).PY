def delete(self, key):
    temp = self.head

    while temp and temp.data != key:
        temp = temp.next

    if temp is None:
        print("Value not found")
        return

    if temp.prev:
        temp.prev.next = temp.next
    else:
        self.head = temp.next

    if temp.next:
        temp.next.prev = temp.prev
