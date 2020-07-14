"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        self.length += 1
        new_node = ListNode(value, None, self.head)
        current = self.head
        if not current:
            self.head = new_node
            self.tail = new_node
        else:
            self.head = new_node
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        current = self.head
        if not current:
            return None
        elif not current.prev:
            self.length -= 1
            result = self.head
            self.head = self.head.next
            self.tail = self.tail.prev
            return result.value
        else:
            self.length -= 1
            result = self.head
            self.head = self.head.next
            return result.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        self.length += 1
        new_node = ListNode(value, self.tail)
        cur = self.head
        if not cur:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        current = self.tail
        if not current:
            return None
        elif not current.prev:
            self.length -= 1
            result = self.head
            self.head = self.head.next
            self.tail = self.tail.prev
            return result.value
        else:
            self.length -= 1
            result = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            return result.value
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        current = self.head
        if current:
            while current.next != None:
                if current.value == node.value:
                    self.add_to_tail(current.value)
                    current.next.prev = current.prev
                    current.prev.next = current.next
                    current = None
                    return
                current = current.next
        return

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        current = self.head
        if current:
            while current.next != None:
                if current.value == node.value:
                    self.add_to_tail(current.value)
                    current.next.prev = current.prev
                    current.prev.next = current.next
                    self.length -= 1
                    current = None
                    return
                current = current.next
        return

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        current = self.head
        if not current:
            return
        elif node.value == self.head.value:
            self.head.next.prev = None
            self.head = self.head.next
            return
        elif node.value == self.tail.value:
            self.tail.prev.next = None
            return
        while current != None:
            if current.value == node.value:
                current.next.prev = current.prev
                current.prev.next = current.next
                current = None
                self.length -= 1
                return
            current = current.next

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        current = self.head
        if current:
            max = current.value
            while current:
                if current.value > max:
                    max = current.value
                current = current.next
            return max
        else:
            return None

    def display(self):
        arr = []
        current = self.head
        if current:
            arr.append(current.value)
            while current.next != None:
                current = current.next
                arr.append(current.value)

        print(arr)


d = DoublyLinkedList(ListNode(1))

d.add_to_tail(20)
d.display()
print(d.get_max())
print(len(d))
