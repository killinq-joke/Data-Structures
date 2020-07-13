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
        self.tail = Node()

    def append(self, value):
        current = self.head
        while current.next != None:
            current = current.next
        current.next = Node(value)

    def add_to_tail(self, tail):
        self.tail = tail

    def remove_head(self):
        self.head.set_value(self.head.get_next())
        self.head.set_next(self.head.next.get_next())

    def get_max(self):
        return "max"

l = LinkedList()

l.remove_head()
print(l.head.value)