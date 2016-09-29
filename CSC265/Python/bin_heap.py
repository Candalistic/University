class BinHeap:
    def __init__(self, root, parent=None):
        """
        Binary heap data structure. It is a complete binary tree, where the maximum element is the root. Elements
        in every level are less than or equal to all of the elements in the upper level.
        """
        self.root = root
        self.parent = parent
        self.left = None
        self.right = None

    def return_max(self):
        """
        Returns the maximum element of the heap, which is the root, according to max-heap property.
        """
        return self.root

    def insert(self, item):
        """
        Inserts the item in its proper position.
        Implementation details:
        First, it inserts the item in the leftmost available space (keeping the tree balanced).
        Then the item is swapped with its parents until it takes its proper place, i.e. until the max-heap property is
        satisfied.
        """
        tree = self
        while tree.left is not None and tree.right is not None:
            tree = tree.left
        if tree.left is None:
            tree.left = BinHeap(item, tree)
            tree = tree.left
        else:
            tree.right = BinHeap(item, tree)
            tree = tree.right
        while (tree.parent is not None) and (tree.parent.root < tree.root):
            a = tree.root
            tree.root = tree.parent.root
            tree.parent.root = a
            tree = tree.parent

    def extract_max(self):
        """
        The same as 'max', but it also removes the root from the heap.
        Implementation details:
        First, replaces root with one of the elements at the end of the tree.
        If the last complete level has no children, then replaces the root with the right element of the last left branch,
        i.e. the 2nd leaf from the left is moved to the root position.
        Else, the last complete level has only one child, on the left, by complete tree definition. In this case, replace
        root with that child.

        After that, the new root is bubbled down to its proper position, i.e. it is moved down until max-heap property
        is restored.
        """
        tree = self
        max = self.root
        while tree.left is not None and tree.right is not None:
            tree = tree.left
        # The last complete level has no children
        if tree.parent.right is not None:
            parent_tree = tree.parent
            tree = tree.parent.right
            parent_tree.right = None
            self.root = tree.root
        # Last complete level has a child on the left
        else:
            parent_tree = tree.parent
            tree =self
            parent_tree.left = None
            self.root = tree.root
        tree = self
        while tree.root < tree.left.root or tree.root < tree.right.root:
            if tree.root < tree.left.root:
                tmp = tree.root
                tree.root = tree.left.root
                tree.left.root = tmp
            else:
                tmp = tree.root
                tree.root = tree.right.root
                tree.right.root = tmp
        return max

    def __len__(self):
        """
        Returns the number of elements in the binary heap
        Implementation details:
        Counts # of objects using Depth-First Search
        """
        if self.left is None and self.right is None:
            return 1
        count = 1
        if self.left is not None:
            count += len(self.left)
        if self.right is not None:
            count += len(self.right)
        return count

    def __str__(self):
        """
        Displays the Heap in levels, like this:
        18
        7 9
        3 5
        2
        Since a complete binary tree is a very strict data structure, there should be no ambiguity in child-parent
        relations here.
        Implementation details:
        Uses breadth-first search.
        """
        s = ''
        from queue import Queue
        displayed = 0
        curr_level = 1
        queue = Queue()
        queue.enqueue(self)
        while not queue.isEmpty():
            current = queue.dequeue()
            displayed += 1
            s += str(current.root) + ' '
            if displayed == 2**(curr_level - 1):
                s += '\n'
                displayed = 0
                curr_level += 1
            if current.left is not None:
                queue.enqueue(current.left)
            if current.right is not None:
                queue.enqueue(current.right)
        return s


if __name__ == '__main__':
    heap = BinHeap(18)
    heap.insert(5)
    heap.insert(9)
    print(heap)
    heap.insert(20)
    heap.insert(10)
    print('Size of the heap is :' + str(len(heap)))
    print(heap)
    print('Max extracted: ' + str(heap.extract_max()))
    print(heap)
