class LRUCache:

    class DoubleLinkedList:
        def _init_(self, data, prev, next):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.exists = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.exists:
            return -1

        if self.exists[key] == self.tail:
            return self.exists[key].data[1]

        self.exists[key].next.prev = self.exists[key].prev
        if self.exists[key] != self.head:
            self.exists[key].prev.next = self.exists[key].next
        else:
            self.head = self.head.next

        self.tail.next = self.exists[key]
        self.exists[key].prev = self.tail
        self.exists[key].next = None
        self.tail = self.tail.next
        return self.exists[key].data[1]

    def put(self, key: int, value: int) -> None:
        
        if key not in self.exists:
            if self.capacity == 0:
                if self.head:
                    del self.exists[self.head.data[0]]
                    self.head = self.head.next
                    
                if self.head == None:
                    self.tail = None
                self.capacity += 1

            if not self.head and not self.tail:
                self.head = self.DoubleLinkedList()
                self.head.data = (key, value)
                self.head.next = None
                self.head.prev = None
                self.tail = self.head
            else:
                curr = self.tail
                self.tail = self.DoubleLinkedList()
                self.tail.data = (key, value)
                self.tail.next = None
                self.tail.prev = curr
                curr.next = self.tail

            self.exists[key] = self.tail
            self.capacity -= 1

        else:
            if self.exists[key] != self.tail:
                self.exists[key].next.prev = self.exists[key].prev
                if self.exists[key] != self.head:
                    self.exists[key].prev.next = self.exists[key].next
                else:
                    self.head = self.head.next

                self.tail.next = self.exists[key]
                self.exists[key].prev = self.tail
                self.exists[key].next = None
                self.tail = self.tail.next

            self.tail.data = (key, value)

            



            



