class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        first = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = first
        first.prev = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        last = self.tail.prev
        last.next = newNode
        newNode.prev = last
        newNode.next = self.tail
        self.tail.prev = newNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        elif index <= 0:
            self.addAtHead(val)
            return
        elif index == self.size:
            self.addAtTail(val)
            return

        newNode = ListNode(val)
        curr = self.head
        for _ in range(index):
            curr = curr.next

        beforeCurr = curr.prev
        beforeCurr.next = newNode
        newNode.prev = beforeCurr
        newNode.next = curr
        curr.prev = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next
        
        toDelete = prev.next
        afterDelete = toDelete.next
        prev.next = afterDelete
        afterDelete.prev = prev
        self.size -= 1