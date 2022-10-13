from cmath import inf


class Heap:
    def __init__(self, a):
        self.heap = self.build_min_heap(a)
        self.size = len(a)

    def build_min_heap(self, a):
        for i in range(int(len(a) / 2) - 1, -1, -1):
            self.min_heapify(a, i)
        return a

    def min_heapify(self, a, i):
        l = 2 * (i + 1) - 1
        r = 2 * (i + 1)

        if l <= len(a) - 1 and a[l].key < a[i].key:
            minim = l
        else:
            minim = i
        if r <= len(a) - 1 and a[r].key < a[minim].key:
            minim = r
        if minim != i:
            swap(a, i, minim)
            self.min_heapify(a, minim)

    def heap_minimum(self):
        return self.heap[0].key

    def heap_extract_min(self):
        if self.size < 1:
            print("error: heap underflow")
        minim = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size = self.size - 1
        self.heap = self.heap[:self.size]
        self.min_heapify(self.heap, 0)
        return minim

    def heap_decrease_key(self, i, key):
        if key > self.heap[i].key:
            print("error: new key is bigger than current one")
        self.heap[i].key = key
        while i > 0 and self.heap[int(i-1 / 2)].key > self.heap[i].key:
            swap(self.heap, i, int(i-1 / 2))
            i = int(i-1 / 2)

    def min_heap_insert(self, vertex):
        key = vertex.key
        self.size = self.size + 1
        self.heap.append(vertex)
        self.heap[self.size - 1].key = inf
        self.heap_decrease_key(self.size - 1, key)

    def print_heap(self):
        print(self.heap)

    def find_node(self, v):
        for i in range(self.size):
            if self.heap[i].node == v:
                return i
        return False


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
