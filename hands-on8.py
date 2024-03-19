def separate(arr, low, high):
    pivot = arr[high]
    i = low - 1
    j = low
    while j < high:
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickfind(arr, low, high, i):
    if low == high:
        return arr[low]
    pivot_index = separate(arr, low, high)
    k = pivot_index - low + 1
    if i == k:
        return arr[pivot_index]
    elif i < k:
        return quickfind(arr, low, pivot_index - 1, i)
    else:
        return quickfind(arr, pivot_index + 1, high, i - k)

def ith_statistic(arr, i):
    return quickfind(arr, 0, len(arr) - 1, i)

# Example
arr = [3, 2, 1, 5, 4]
i = 3
print(f"The {i}th order statistic is: {ith_statistic(arr, i)}")

class StackModified:
    def __init__(self, size):
        self.size = size
        self.data = [0] * size
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.size - 1

    def push(self, item):
        if self.isFull():
            print("Stack Overflow")
            return
        self.top += 1
        self.data[self.top] = item

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return None
        item = self.data[self.top]
        self.top -= 1
        return item

class QueueModified:
    def __init__(self, size):
        self.size = size
        self.data = [0] * size
        self.front = 0
        self.rear = -1
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size

    def enqueue(self, item):
        if self.isFull():
            print("Queue Overflow")
            return
        self.rear = (self.rear + 1) % self.size
        self.data[self.rear] = item
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return None
        item = self.data[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return item

class NodeModified:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class SinglyLinkedListModified:
    def __init__(self):
        self.headNode = None

    def insertStart(self, data):
        newNode = NodeModified(data)
        newNode.nextNode = self.headNode
        self.headNode = newNode

    def deleteStart(self):
        if self.headNode is None:
            print("List is empty")
            return None
        data = self.headNode.data
        self.headNode = self.headNode.nextNode
        return data

    def display(self):
        current = self.headNode
        while current:
            print(current.data, end=" -> ")
            current = current.nextNode
        print("None")

# Examples of Stack, Queue, and Singly Linked List
stack = StackModified(5)
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.pop())

queue = QueueModified(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
print(queue.dequeue())

linked_list = SinglyLinkedListModified()
linked_list.insertStart(1)
linked_list.insertStart(2)
linked_list.insertStart(3)
linked_list.display()
linked_list.deleteStart()
linked_list.display()
