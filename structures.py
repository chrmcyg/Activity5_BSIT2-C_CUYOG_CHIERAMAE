"""Stacks and queues built from first principles (array and linked list)."""


class Node:
    """Singly linked list node shared by LinkedStack and LinkedQueue."""
    def __init__(self, value):
        self.value = value
        self.next = None


class ArrayStack:
    """Fixed-capacity stack on a Python list. top == -1 means empty."""
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.data) - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow: cannot push onto a full stack")
        self.top = self.top + 1          # move top up first
        self.data[self.top] = value      # then store

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack")
        value = self.data[self.top]      # read first
        self.top = self.top - 1          # then move top down
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: nothing to peek")
        return self.data[self.top]

    def __str__(self):
        return "Stack (bottom -> top): " + str(self.data[:self.top + 1])


class LinkedStack:
    """Unbounded stack; push/pop at the head so both are O(1)."""
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return False  # limited only by memory

    def push(self, value):
        node = Node(value)
        node.next = self.top   # new node points to old top
        self.top = node        # new node becomes top

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: nothing to peek")
        return self.top.value

    def __str__(self):
        items, cur = [], self.top
        while cur:
            items.append(cur.value)
            cur = cur.next
        return "Stack (bottom -> top): " + str(items[::-1])


class ArrayQueue:
    """Circular queue; a size counter distinguishes empty from full."""
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.front = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.data)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue overflow: cannot enqueue into a full queue")
        rear = (self.front + self.size) % len(self.data)  # wrap around
        self.data[rear] = value
        self.size = self.size + 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue")
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)    # wrap around
        self.size = self.size - 1
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: nothing to peek")
        return self.data[self.front]

    def __str__(self):
        items = [self.data[(self.front + i) % len(self.data)] for i in range(self.size)]
        return f"Queue (front -> rear): {items}  | raw array: {self.data}, front index={self.front}"


class LinkedQueue:
    """Queue with head (front) and tail (rear) references; both ops O(1)."""
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return False

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
        else:
            self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:   # queue became empty -> reset rear too
            self.rear = None
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: nothing to peek")
        return self.front.value

    def __str__(self):
        items, cur = [], self.front
        while cur:
            items.append(cur.value)
            cur = cur.next
        return "Queue (front -> rear): " + str(items)
