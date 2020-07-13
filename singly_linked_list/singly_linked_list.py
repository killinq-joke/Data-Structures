class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = None

    def add_to_tail(self, value):

        new_node = Node(value)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
        

    def remove_head(self):
        value = self.head.get_value()
        if not self.head:
            return None
        if self.tail is self.head:
            self.tail = None
            self.head = None
            return value
        self.head = self.head.next
        return value

    def contains(self, value):
        current = self.head
        if not current:
            return None
        while current.next != None:
            if current.value == value:
                return True
            current = current.next
        return False

    def get_max(self):
        current = self.head
        arr = []
        while current.get_next() != None:
            arr.append(current.value)
        return max(arr)

    def remove_tail(self):
        if not self.head:
            return None

        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value

        current = self.head
        while current.get_next() is not self.tail:
            current = current.get_next()
        value = self.tail.get_value()
        self.tail = current
        self.tail.set_next(None)
        return value

    def display(self):
        arr = []
        cur_node = self.head
        if cur_node:
            while cur_node.next != None:
                cur_node = cur_node.next
                arr.append(cur_node.value)
        print(arr)


l = LinkedList()

l.add_to_tail(20)
l.add_to_tail(20)
l.add_to_tail(20)

l.display()
