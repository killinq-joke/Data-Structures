class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next

     
class LinkedList:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail