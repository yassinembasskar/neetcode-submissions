class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.max_length = k
        self.length = 0

    def enQueue(self, value: int) -> bool:
        if self.length == self.max_length:
            return False
        if not self.tail and not self.head:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        self.length += 1
        return True

    def deQueue(self) -> bool:
        if not self.head:
            return False
        self.head = self.head.next
        if not self.head:
            self.tail = None
        else :
            self.head.prev = None
        self.length -= 1
        return True

    def Front(self) -> int:
        if not self.head:
            return -1
        return self.head.value

    def Rear(self) -> int:
        if not self.tail:
            return -1
        return self.tail.value

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.max_length


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()