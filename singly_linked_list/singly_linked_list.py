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
        self.head = None
        self.tail = None

    def add_to_tail(self, value):

        if not self.tail:
            self.tail = Node(value)
        else:
            self.tail.set_next(Node(value))
            self.tail = Node(value)

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
        while current.next != None:
            if current.value == value:
                return True
            current = current.next
        return False

    def get_max(self):
        current = self.head
        arr = []
        while current.value != None:
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
