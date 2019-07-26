class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item
        self.current += 1

        if self.current == len(self.storage):
            self.current = 0

    def get(self):
        list = [i for i in self.storage if i is not None]
        return list
