class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, value):
        new_node = Node(value)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def __len__(self):
        current = self.head
        total = 0
        while current.next != None:
            total += 1
            current = current.next
        return total

    def add_to_tail(self, tail):
        self.tail = tail

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.value)
        print(elems)

    def get_max(self):
        return "max"

    def get(self, index):
        if index >= self.__len__():
            print("get error")
            return None
        else:
            cur_idx = 0
            current = self.head
            while True:
                if cur_idx == index:
                    return current.value
                else:
                    current = current.next
                    cur_idx += 1


l = LinkedList()
l.append(1)
l.append(2)
l.append(10)
l.append(4)
l.display()
