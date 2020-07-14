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

    def __len__(self):
        current = self.head
        length = 0
        if current:
            length += 1
            while current.next != None:
                length += 1
                current.prev = current
                current = current.next
        return length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
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
            result = self.head
            self.head = self.head.next
            self.tail = self.tail.prev
            return result.value
        else:
            result = self.head
            self.head = self.head.next
            return result.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
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
            result = self.head
            self.head = self.head.next
            self.tail = self.tail.prev
            return result.value
        else:
            result = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            return result.value
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        pass

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        current = self.head
        if current:
            max = current.value
            while current.next != None:
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

d.remove_from_tail()
print(d.tail)
d.display()
print(d.get_max())
print(len(d))
