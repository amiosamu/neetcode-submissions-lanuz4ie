class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        

    def append(self, value: int) -> None:
        new_node = Node(value)
        last = self.tail.prev

        last.next = new_node
        new_node.prev = last
        new_node.next = self.tail
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)

        first = self.head.next

        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first
        first.prev = new_node 

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        last = self.tail.prev
        value = last.value
        prev_node = last.prev

        prev_node.next = self.tail
        self.tail.prev = prev_node
        return value
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        first = self.head.next
        value = first.value
        next_node = first.next

        self.head.next = next_node
        next_node.prev = self.head
        return value
        
