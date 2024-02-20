class MinHeap:
    def __init__(self):
        self.data = []

    def get_parent(self, idx):
        return (idx - 1) >> 1

    def get_left_child(self, idx):
        return (idx << 1) + 1

    def get_right_child(self, idx):
        return (idx << 1) + 2

    def build_heap(self, arr):
        self.data = arr
        n = len(self.data)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(i)

    def heapify_down(self, idx):
        while True:
            left = self.get_left_child(idx)
            right = self.get_right_child(idx)
            smallest_idx = idx if left >= len(self.data) or self.data[left] >= self.data[idx] else left
            smallest_idx = smallest_idx if right >= len(self.data) or self.data[right] >= self.data[smallest_idx] else right
            if smallest_idx != idx:
                self.data[idx], self.data[smallest_idx] = self.data[smallest_idx], self.data[idx]
                idx = smallest_idx
            else:
                break

    def heapify_up(self, idx):
        while idx > 0 and self.data[self.get_parent(idx)] > self.data[idx]:
            parent_idx = self.get_parent(idx)
            self.data[idx], self.data[parent_idx] = self.data[parent_idx], self.data[idx]
            idx = parent_idx

    def insert(self, item):
        self.data.append(item)
        self.heapify_up(len(self.data) - 1)

    def pop(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()
        root = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return root

# Example :
heap = MinHeap()
heap.build_heap([4, 7, 1, 3, 9, 5])
print("Initial heap:", heap.data)

heap.insert(2)
print("After inserting 2:", heap.data)

print("Popping root:", heap.pop())
print("After popping root:", heap.data)
