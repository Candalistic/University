from bin_heap import BinHeap


class PriorityQueue:
    def __init__(self, items):
        self.bin_heap = BinHeap(items[0])
        for item in items:
            self.bin_heap.insert(item)

    def max(self):
        return self.bin_heap.return_max()

    def extract_max(self):
        return self.bin_heap.extract_max()

    def insert(self, item):
        self.bin_heap.insert(item)

    def __str__(self):
        return str(self.bin_heap)


if __name__ == '__main__':
    from random import Random
    r = Random()
    q = PriorityQueue([i for i in range(10)])
    print(q)
    print(q.extract_max())
    print(q)
