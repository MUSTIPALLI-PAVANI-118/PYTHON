def display(self):
    if self.head is None:
        print("List is empty")
        return

    temp = self.head
    while True:
        print(temp.data, end=" -> ")
        temp = temp.next
        if temp == self.head:
            break
    print("(back to head)")
