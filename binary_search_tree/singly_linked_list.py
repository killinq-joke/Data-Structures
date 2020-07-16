class Node:
    def __init__(self, value=None, next=None):
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
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):

        new_node = Node(value)
        cur = self.head
        if not cur:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        # return None if there is no head (i.e. the list is empty)
        if not self.head:
            return None
        # if head has no next, then we have a single element in our list
        if not self.head.get_next():
            # get a reference to the head
            head = self.head
            # delete the list's head reference
            self.head = None
            # also make sure the tail reference doesn't refer to anything
            self.tail = None
            # return the value
            return head.get_value()
        # otherwise we have more than one element in our list
        value = self.head.get_value()
        # set the head reference to the current head's next node in the list
        self.head = self.head.get_next()
        return value

    def contains(self, value):
        current = self.head
        if not current:
            return False
        while True:
            if current.value == value:
                return True
            current = current.next
            if current == None:
                return False

    def get_max(self):
        if not self.head:
            return None

        max_value = self.head.get_value()

        current = self.head.get_next()

        while current:

            if current.get_value() > max_value:

                max_value = current.get_value()

            current = current.get_next()
        return max_value

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
        current = self.head
        arr.append(current.value)
        if current:
            while current.next != None:
                current = current.next
                arr.append(current.value)

        print(arr)

    def __len__(self):
        current = self.head
        total = 0
        if current:
            total += 1
            while current.next != None:
                total += 1
                current = current.get_next()
        return total
