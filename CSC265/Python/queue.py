class Queue:
    """A simple queue class"""
    def __init__(self):
        self.lst = []

    def enqueue(self, item):
        self.lst.append(item)

    def dequeue(self):
        return self.lst.pop(0)

    def isEmpty(self):
        return len(self.lst) == 0
