class Queue:
    stack1: list
    stack2: list

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def append(self, val):
        self.stack1.append(val)

    def pop(self):
        if self.size() == 0:
            return -1

        if len(self.stack2) == 0:
            self.rebuild()

        return self.stack2.pop()

    def rebuild(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

    def size(self):
        return len(self.stack1) + len(self.stack2)

    def peek(self):
        if self.size() == 0:
            return -1
        if len(self.stack2) == 0:
            self.rebuild()

        return self.stack2[-1]

queue = Queue()

print(queue.peek())
print(queue.pop())
print(queue.append(1))
print(queue.append(2))
print(queue.append(3))
print(queue.peek())
print(queue.pop())
print(queue.pop())
print(queue.size())
print(queue.append(4))
print(queue.append(5))
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())
