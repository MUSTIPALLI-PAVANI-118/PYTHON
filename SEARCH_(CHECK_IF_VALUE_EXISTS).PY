def search(self, key):
    if self.head is None:
        return False

    temp = self.head
    while True:
        if temp.data == key:
            return True
        temp = temp.next
        if temp == self.head:
            break
    return False
